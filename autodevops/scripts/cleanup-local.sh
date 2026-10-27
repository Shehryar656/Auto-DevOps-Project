#!/usr/bin/env bash
set -Eeuo pipefail
echo "This removes only the local demo container named autodevops-ui."
echo "It does not delete images, Kubernetes resources, volumes or project files."
read -r -p "Continue? Type yes: " answer
if [ "$answer" = "yes" ]; then
  sudo docker rm -f autodevops-ui 2>/dev/null || true
  echo "Local demo container cleanup completed."
else
  echo "Cancelled."
fi
