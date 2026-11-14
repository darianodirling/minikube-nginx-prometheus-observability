# Architecture decisions

## ADR-001: Minikube and ingress-nginx
**Decision:** Use Minikube with ingress and metrics-server add-ons to make the lab reproducible on a laptop. **Tradeoff:** Not a production HA topology.

## ADR-002: NGINX exporter sidecar
**Decision:** Co-locate exporter with NGINX and scrape loopback stub_status. **Tradeoff:** One exporter per pod; exporter lifecycle is tied to workload.

## ADR-003: Kubernetes service discovery
**Decision:** Prometheus discovers exporter containers from pod metadata, avoiding hardcoded pod IPs. **Tradeoff:** Requires pod-list/watch RBAC in the namespace.

## ADR-004: CPU-based HPA
**Decision:** Use standard metrics-server CPU utilization rather than a custom Prometheus Adapter. **Tradeoff:** Prometheus charts are observational; scaling does not directly depend on request rate.

## ADR-005: Ephemeral TSDB
**Decision:** Use emptyDir for minimal setup. **Tradeoff:** Historical metrics disappear after pod recreation. Use a PVC and retention sizing for durable environments.
