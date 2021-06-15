# Using k8s redis config

## Redis install 
```
helm install <my-release> bitnami/redis
```

## Get Password
```
export REDIS_PASSWORD=$(kubectl get secret --namespace default my-release-redis -o jsonpath="{.data.redis-password}" | base64 --decode)
```
