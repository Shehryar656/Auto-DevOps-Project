# Operations runbook

## Check local Docker container

    sudo docker ps
    sudo docker logs --tail 100 autodevops-ui
    curl -fsS http://127.0.0.1:18081/health

## Check K3s

    sudo k3s kubectl get nodes
    sudo k3s kubectl get pods -A

## Troubleshoot local image

    sudo docker build -t autodevops-demo:1.1.0 .
    sudo docker image ls autodevops-demo

## Safety

Inspect the target namespace and manifests before applying changes.
Do not delete namespaces, persistent volumes or production resources as a
generic recovery action. Back up state and require approval for destructive work.
