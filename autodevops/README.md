# AutoDevOps — Reusable DevOps Starter

A portfolio-ready learning project for containerized application delivery.
It provides a demo dashboard, Docker build, real HTTP smoke tests, a GitHub
Actions CI workflow, Trivy image scanning, Kubernetes starter manifests,
and a Helm chart starter.

## Features

- Responsive animated engineering dashboard.
- Python HTTP backend with `/health` and `/api/status`.
- Non-root Docker container.
- GitHub Actions: build, health test, dashboard smoke test, Trivy scan.
- K3s manifests and a Helm chart starter.
- Operational runbooks and cautious deployment/rollback scripts.

## Current status — read before use

**Implemented:** local Docker build, application health endpoints, GitHub
Actions CI workflow, container smoke tests and Trivy scan job.

**Starter templates:** Kubernetes deployment scripts and Helm chart. Review
the image name, cluster access, manifests and image-pull settings before use.

**Roadmap:** publishing versioned images to GHCR, automated Kubernetes delivery,
Prometheus/Grafana dashboards and alerts, and controlled remediation.

The dashboard's animated pipeline is a visual simulation. Clicking it does
not execute GitHub Actions or deploy to Kubernetes.

## Application contract

To reuse this template, the application container should:
- listen on `0.0.0.0:8080`;
- return HTTP 200 at `/health`;
- serve its main page or API at `/`;
- include any required runtime and dependencies in the Dockerfile.

Replacing only `app/` works when the replacement follows this contract and
the existing runtime. For a different language or framework, adapt the
Dockerfile and tests too.

## Run locally

Build the image:

    sudo docker build -t autodevops-demo:1.1.0 .

Run the dashboard:

    sudo docker rm -f autodevops-ui 2>/dev/null || true
    sudo docker run -d --name autodevops-ui --restart unless-stopped -p 18081:8080 autodevops-demo:1.1.0

Verify:

    curl -fsS http://localhost:18081/health
    curl -fsS http://localhost:18081/api/status

Open `http://localhost:18081` in your browser.

## GitHub CI

The workflow is `.github/workflows/ci.yml`. It runs on pushes to `main`,
pull requests targeting `main`, and manual dispatch. It builds the image,
starts a temporary container, tests the health endpoint, checks the dashboard,
and scans the image with Trivy.

To view results: GitHub repository -> Actions -> AutoDevOps CI -> select a run
-> select the `Build, test and scan` job to inspect every step and its logs.

The Trivy job initially reports HIGH/CRITICAL findings without failing the
workflow. Review findings and harden the policy before using it for production.

## Kubernetes and Helm

Review the manifests in `k8s/` and `helm/autodevops/` before deploying.
The Helm values currently use a placeholder image repository. A published
image and appropriate cluster access are required for a real deployment.

A GitHub-hosted runner cannot automatically access a private local WSL2 K3s
cluster. Configure a secure deployment runner or a deliberate deployment
architecture before adding automated CD.

## Security

Never commit secrets, `.env` files, credentials or private keys. The Docker
group grants root-equivalent privileges. Production changes and destructive
operations should require least privilege, review and approval.

## License

This project is provided as a learning starter. Add a license before
redistributing it as an open-source template.
