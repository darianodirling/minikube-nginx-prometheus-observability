# KCNA lab evidence checklist

This is a **blank verification tracker**. Mark tasks complete only after running the lab and capturing redacted evidence.

| Done | Phase | Milestone | Suggested evidence |
| --- | --- | --- | --- |
| [ ] | 1 | Docker, kubectl, Minikube, Helm installed | Version outputs |
| [ ] | 1 | Two nodes Ready and Calico active | `kubectl get nodes -o wide`; Calico pods |
| [ ] | 2 | Broken image diagnosed and removed | Redacted ImagePullBackOff events |
| [ ] | 2 | NGINX rollout and scaling completed | `kubectl rollout history deploy/webapp` |
| [ ] | 2 | DaemonSet and Job verified | `kubectl get ds,jobs` |
| [ ] | 3 | ConfigMap and Secret injected | Pod spec showing references, **not secret values** |
| [ ] | 3 | Startup/liveness/readiness probes verified | `kubectl describe pod configured-pod` |
| [ ] | 4 | Worker taint, toleration and affinity tested | `kubectl get pod scheduled-pod -o wide` |
| [ ] | 4 | Redis StatefulSet, PVC and PDB observed | `kubectl get sts,pvc,pdb` |
| [ ] | 5 | API proxy and RBAC allow/deny verified | `kubectl auth can-i` outputs |
| [ ] | 5 | Restricted PSA and ResourceQuota tested | `kubectl describe quota -n secure-ns` |
| [ ] | 6 | Ingress and Gateway API CRDs inspected | `kubectl get ingress,crds` |
| [ ] | 6 | NetworkPolicy denies/permits verified | Labeled/unlabeled test pod outputs |
| [ ] | 6 | Kustomize overlay applied | `kubectl get deploy -l managed-by=kustomize` |
| [ ] | 6 | Helm monitoring stack installed | `helm list -n monitoring`; Grafana screenshot |
| [ ] | 6 | ArgoCD console reachable | Redacted UI screenshot |

## Exercise log template

- Date and environment:
- Ubuntu / Docker / Minikube / kubectl / Helm versions:
- Cluster node resources:
- Phase and objective:
- Commands executed:
- Observed output (redacted):
- Unexpected behavior:
- Troubleshooting and resolution:
- Evidence file or screenshot:
- Completion status: Not started / In progress / Verified

Do not commit kubeconfig files, tokens, password output, certificates or sensitive IPs.
