# Monitoring roadmap

Planned components:
- Prometheus for metrics collection.
- Grafana for dashboards.
- Alert rules for availability, restarts and resource pressure.
- Application logs and documented diagnostic runbooks.

Current implementation:
- HTTP `/health` endpoint.
- HTTP `/api/status` endpoint.
- CI smoke tests.

Prometheus and Grafana are not installed or configured by this document.
They will be added and verified in a later project stage.
