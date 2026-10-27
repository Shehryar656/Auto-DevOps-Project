from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime, timezone
from pathlib import Path
import json
import socket

APP_DIR = Path(__file__).resolve().parent

class Handler(BaseHTTPRequestHandler):
    def respond(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy",
                         "default-src 'self'; style-src 'self' 'unsafe-inline'; "
                         "script-src 'self' 'unsafe-inline'; connect-src 'self'; "
                         "img-src 'self' data:; base-uri 'none'; frame-ancestors 'none'")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            file = APP_DIR / "index.html"
            if not file.is_file():
                return self.respond(500, b"Dashboard file missing", "text/plain; charset=utf-8")
            return self.respond(200, file.read_bytes(), "text/html; charset=utf-8")

        if self.path == "/health":
            data = {
                "status": "healthy",
                "service": "autodevops-demo",
                "hostname": socket.gethostname(),
                "time": datetime.now(timezone.utc).isoformat()
            }
            return self.respond(200, json.dumps(data).encode(), "application/json; charset=utf-8")

        if self.path == "/api/status":
            data = {
                "service": "autodevops-demo",
                "health": "healthy",
                "pipeline_mode": "simulation",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
            return self.respond(200, json.dumps(data).encode(), "application/json; charset=utf-8")

        return self.respond(404, b'{"error":"not found"}', "application/json; charset=utf-8")

    def log_message(self, fmt, *args):
        print(f"{self.address_string()} - {fmt % args}", flush=True)

if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8080), Handler)
    print("AutoDevOps dashboard listening on port 8080", flush=True)
    server.serve_forever()
