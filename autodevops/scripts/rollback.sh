#!/usr/bin/env bash
set -Eeuo pipefail

NAMESPACE="${1:-autodevops}"
DEPLOYMENT="${2:-autodevops-demo}"

echo "Target namespace: $NAMESPACE"
echo "Target deployment: $DEPLOYMENT"
sudo k3s kubectl get deployment "$DEPLOYMENT" -n "$NAMESPACE"
echo
sudo k3s kubectl rollout history deployment/"$DEPLOYMENT" -n "$NAMESPACE"
echo
read -r -p "Undo the latest rollout? Type yes: " answer
if [ "$answer" != "yes" ]; then
  echo "Cancelled."
  exit 0
fi
sudo k3s kubectl rollout undo deployment/"$DEPLOYMENT" -n "$NAMESPACE"
sudo k3s kubectl rollout status deployment/"$DEPLOYMENT" -n "$NAMESPACE" --timeout=120s
