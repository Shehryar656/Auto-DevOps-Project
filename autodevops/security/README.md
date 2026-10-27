# Security

The CI workflow runs Trivy against the built container image and reports
HIGH and CRITICAL vulnerabilities.

Initial learning mode uses `exit-code: '0'`, so findings are visible without
automatically blocking the pipeline. After reviewing and fixing findings,
consider changing it to `exit-code: '1'`.

Security checklist:
- Never commit secrets, tokens, private keys or real `.env` files.
- Use a non-root application user inside the container.
- Pin dependencies and review base-image updates.
- Review Trivy findings; do not blindly suppress them.
- Give CI and Kubernetes only the permissions they need.
- Require human approval for destructive production actions.

This scan is one security check, not proof that the application is completely
secure.
