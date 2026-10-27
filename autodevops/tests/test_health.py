"""Smoke test for the running AutoDevOps application."""
import json
import os
import urllib.error
import urllib.request

base_url = os.getenv("BASE_URL", "http://127.0.0.1:18080").rstrip("/")

def get_json(path):
    request = urllib.request.Request(
        base_url + path,
        headers={"Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=5) as response:
        assert response.status == 200, f"Unexpected HTTP status: {response.status}"
        return json.load(response)

health = get_json("/health")
assert health.get("status") == "healthy", health
assert health.get("service") == "autodevops-demo", health
print("PASS: /health returns a healthy application response")

status = get_json("/api/status")
assert status.get("health") == "healthy", status
print("PASS: /api/status returns application status")
