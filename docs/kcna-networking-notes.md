# KCNA networking and security notes

## Calico and NetworkPolicy

The lab uses `--cni=calico` because Kubernetes NetworkPolicy requires a compatible enforcing CNI. The Phase 6 exercise permits inbound traffic to `app=webapp` Pods only from same-namespace Pods with label `access=granted`.

**Important:** An ingress controller typically runs in `ingress-nginx`, not `kcna-lab`. A same-namespace podSelector-only allow rule does not permit ingress-controller traffic. This is expected when demonstrating isolation; add a carefully scoped namespaceSelector/podSelector rule if the goal is to allow ingress traffic too.

## Gateway API

The workbook installs Gateway API CRDs. Installing CRDs creates API types but does not provide a controller or active traffic routing. A GatewayClass/controller and suitable Gateway/HTTPRoute resources would be needed for a complete Gateway API demonstration.

## Security

- Use EAP/TLS concepts only where relevant; the Kubernetes lab's identity control is Kubernetes RBAC and ServiceAccounts.
- Keep secrets out of screenshots and git history. The workbook uses a simple example secret for teaching; substitute a disposable value.
- Pod Security Admission `restricted` needs non-root UID, seccomp RuntimeDefault and dropped capabilities as demonstrated in Phase 5.
- Test RBAC in the intended namespace, with the service account subject qualified as `system:serviceaccount:kcna-lab:pod-reader-sa`.
- Avoid exposing Grafana, ArgoCD and API proxy beyond localhost during the lab.
