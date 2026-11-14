#!/usr/bin/env python3
"""Offline Kubernetes manifest checks; no cluster access."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
files = [
 "README.md", "k8s/kustomization.yaml", "k8s/namespace.yaml",
 "k8s/nginx-config.yaml", "k8s/deployment.yaml", "k8s/service.yaml",
 "k8s/ingress.yaml", "k8s/hpa.yaml", "k8s/prometheus-rbac.yaml",
 "k8s/prometheus-config.yaml", "k8s/prometheus-deployment.yaml",
 "k8s/prometheus-service.yaml", "docs/architecture-decisions.md",
 "docs/verification.md",
]
missing = [p for p in files if not (root / p).is_file()]
if missing:
    raise SystemExit(f"Missing files: {missing}")
assert "mermaid" in (root / "README.md").read_text()
assert "autoscaling/v2" in (root / "k8s/hpa.yaml").read_text()
assert "kubernetes_sd_configs" in (root / "k8s/prometheus-config.yaml").read_text()
print("PASS: structural checks. Live Minikube deployment not tested.")
