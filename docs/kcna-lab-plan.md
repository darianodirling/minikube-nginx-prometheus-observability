# KCNA six-phase hands-on lab plan

Aligned to the uploaded **KCNA Minikube Hands-On Lab Guide**, pages 1–16. These are exercise objectives and representative commands, **not completed results**.

## Phase 1 — Environment and cluster (15 minutes)
Install Docker Engine, kubectl, Minikube and Helm on Ubuntu Desktop. Configure non-root Docker access. Start two nodes using Docker and Calico.

```bash
minikube start --nodes 2 --cpus 2 --memory 3072 --driver=docker --cni=calico
kubectl get nodes -o wide
kubectl get pods -n kube-system -l k8s-app=calico-node
```

## Phase 2 — Core workloads (25 minutes)
Create `kcna-lab`; deploy a working NGINX pod and an intentionally broken image to diagnose ImagePullBackOff. Create three-replica `webapp`, roll forward the NGINX image and patch replicas to four. Demonstrate a DaemonSet and batch Job.

```bash
kubectl create namespace kcna-lab
kubectl config set-context --current --namespace=kcna-lab
kubectl run web-pod --image=nginx:alpine
kubectl run broken-pod --image=nginx:nonexistent-tag
kubectl describe pod broken-pod
kubectl delete pod broken-pod
kubectl create deployment webapp --image=nginx:1.26-alpine --replicas=3
kubectl set image deployment/webapp nginx=nginx:1.27-alpine
kubectl rollout status deployment/webapp
kubectl patch deployment webapp -p '{"spec":{"replicas":4}}'
```

See workbook pages 3–5 for the DaemonSet and Job examples.

## Phase 3 — Configuration and health (20 minutes)
Create ConfigMap and Secret, inject as environment variables, label/annotate a pod and configure startup, liveness and readiness probes. Do not capture or commit raw secret values.

```bash
kubectl create configmap app-config --from-literal=ENV_MODE=production
# Use a unique disposable value and avoid shell history or committed credentials.
kubectl create secret generic app-secret --from-literal=API_KEY=REPLACE_WITH_LAB_ONLY_VALUE
kubectl describe pod configured-pod
kubectl get pods -l tier=backend,release=stable --show-labels
```

## Phase 4 — Scheduling and state (20 minutes)
Apply `dedicated=special:NoSchedule` taint and `disktype=nvme` label to worker `minikube-m02`; schedule a matching Pod with toleration and required node affinity. Remove taint afterward. Deploy a two-replica Redis StatefulSet, headless Service, dynamic PVC templates and a PDB.

```bash
kubectl taint nodes minikube-m02 dedicated=special:NoSchedule
kubectl label nodes minikube-m02 disktype=nvme
kubectl get pod scheduled-pod -o wide
kubectl taint nodes minikube-m02 dedicated=special:NoSchedule-
kubectl get sts,pods,pvc,pv,pdb
```

## Phase 5 — API and security (20 minutes)
Use `kubectl proxy` for API inspection, create a read-only Pod Role/RoleBinding for `pod-reader-sa`, and verify permitted and denied actions. In `secure-ns`, demonstrate restricted Pod Security Admission, a ResourceQuota and a non-root container.

```bash
kubectl create serviceaccount pod-reader-sa
kubectl create role pod-reader-role --verb=get,list,watch --resource=pods
kubectl create rolebinding pod-reader-binding --role=pod-reader-role --serviceaccount=kcna-lab:pod-reader-sa
kubectl auth can-i list pods --as=system:serviceaccount:kcna-lab:pod-reader-sa
kubectl auth can-i delete pods --as=system:serviceaccount:kcna-lab:pod-reader-sa
kubectl create namespace secure-ns
kubectl label namespace secure-ns pod-security.kubernetes.io/enforce=restricted
```

## Phase 6 — Cloud native ecosystem (20 minutes)
Enable NGINX ingress, expose `webapp`, define host-based routing, install Gateway API CRDs, enforce a Calico NetworkPolicy, demonstrate a Kustomize overlay, install kube-prometheus-stack with Helm, and install ArgoCD.

```bash
minikube addons enable ingress
kubectl expose deployment webapp --port=80 --target-port=80 --name=webapp-svc
kubectl get ingress,networkpolicy
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace --set alertmanager.enabled=false
kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl port-forward svc/argocd-server -n argocd 8443:443
```

**Caution:** External install URLs and chart versions change. Pin and review releases before execution. ArgoCD `stable` is mutable. Verify resource capacity before installing monitoring and GitOps concurrently.

## End of session

```bash
minikube stop    # preserve cluster state
# OR, only when ready to destroy all local cluster data:
# minikube delete
```
