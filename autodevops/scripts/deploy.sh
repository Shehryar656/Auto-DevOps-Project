#!/usr/bin/env bash
set -Eeuo pipefail
cd "$(dirname "$0")/.."

if ! command -v k3s >/dev/null 2>&1; then
  echo "ERROR: k3s command not found."
  exit 1
fi

if [ ! -f k8s/deployment.yaml ]; then
  echo "ERROR: k8s/deployment.yaml is missing."
  exit 1
fi

echo "Reviewing Kubernetes manifests..."
cat k8s/deployment.yaml
echo
read -r -p "Apply this manifest to the current K3s cluster? Type yes: " answer
if [ "$answer" != "yes" ]; then
  echo "Cancelled."
  exit 0
fi

sudo k3s kubectl apply -f k8s/deployment.yaml
echo "Apply command completed. Check resources with:"
echo "sudo k3s kubectl get pods -A"
