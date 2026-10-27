# AutoDevOps architecture

## Delivery flow

Developer push / pull request
    -> GitHub Actions
    -> Docker image build
    -> HTTP health test
    -> Trivy image scan
    -> CI result and logs

## Kubernetes target

K3s is the local Kubernetes target. The cluster deployment is a separate
stage; a GitHub-hosted runner cannot automatically access a private WSL2
cluster. A future deployment stage needs a deliberately configured runner
or another secure deployment path.

## Application contract

For the current container and CI template, an application must:
- Listen on `0.0.0.0:8080`.
- Return HTTP 200 from `/health`.
- Return a dashboard or application response from `/`.
- Include the runtime and dependency setup required by the root Dockerfile.

If you switch to another programming language or runtime, adapt the Dockerfile
and tests to the new application while preserving the contract, or update the
contract and the pipeline together.

## Current truth

The GitHub Actions build, HTTP smoke tests and Trivy scan are real jobs.
The dashboard's animated pipeline is a UI simulation. Kubernetes deployment,
Prometheus/Grafana and automatic remediation are planned integrations.
