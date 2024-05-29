Command example calling Kubernetes API with JSON file:
```bash
curlie -d "@nginx-pod.json" -H "Content-Type: application/json" -X POST http://localhost:8080/api/v1/namespaces/default/pods
```
