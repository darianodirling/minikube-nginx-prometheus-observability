# Verification checklist

1. `kubectl get nodes` shows a Ready node.
2. `kubectl -n ingress-nginx get pods` shows the ingress controller.
3. `kubectl -n kube-system get deploy metrics-server` reports available replicas.
4. `kubectl apply -k k8s/` succeeds.
5. `kubectl -n observability-demo get deploy,pods,svc,ingress,hpa` shows ready resources.
6. Port-forward ingress and curl with the Host header; expect `nginx observability demo`.
7. `kubectl -n observability-demo port-forward svc/prometheus 9090:9090`; check `up{job="nginx"}` in Prometheus.
8. Confirm NGINX exporter metrics increase under request load.
9. Generate sustained CPU load and observe HPA decisions; request load alone may not scale NGINX.
10. Tear down with `kubectl delete -k k8s/` after the exercise.

## Troubleshooting

- **Ingress 404:** check Host header, ingress class, controller and ingress resource.
- **Prometheus targets absent:** inspect pod labels, exporter container/port names and Prometheus logs.
- **HPA unknown CPU:** verify metrics-server and pod CPU requests.
- **Exporter down:** inspect `nginx -T`, stub_status on 8081 and exporter logs.
- **Metrics disappear:** expected with emptyDir after pod replacement.
