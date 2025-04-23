# Kubernetes-App-Deployment-with-TLS-MongoDB

This project demonstrates deploying a Flask web application with a MongoDB backend on a Kubernetes cluster. It includes Ingress, TLS secured by the Kubernetes internal CA, and uses MetalLB for LoadBalancer services.

🚀 Project Overview

1. Flask App Development & Deployment

Developed a simple Flask app (app.py).

Created a Dockerfile to containerize the app.

Pushed the Docker image to Docker Hub.

Deployed the Flask app to Kubernetes using:

Deployment

ClusterIP Service

2. MongoDB Stateful Backend

Created a StatefulSet for MongoDB to maintain stable network identity and persistent storage.

Configured a headless service for MongoDB access within the cluster.

3. Ingress and HTTPS Setup

Configured Ingress using the NGINX Ingress Controller.

Enabled HTTPS:

Generated TLS certificate signed by Kubernetes internal CA using cert-manager.

Attached the certificate to the Ingress resource.

Set up MetalLB to provide a LoadBalancer IP for internal network access.

🔐 Features

✅ Secure app access via HTTPS with Kubernetes CA

✅ Persistent MongoDB backend with stable DNS via StatefulSet

✅ Internal LoadBalancer using MetalLB

✅ Full CI-style deployment: Docker -> Kubernetes


🧪 Try It Yourself

# Deploy NGINX Ingress Controller
#Install NGINX Ingress Controller
||helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
||helm repo update

||helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace

#Check Logs in Ingress Controller
||kubectl logs -n ingress-nginx deploy/ingress-nginx-controller

#Install MetalLB and configure the IP pool: kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.9/config/manifests/metallb-native.yaml
#Create metallb-config.yaml

apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: default-address-pool
  namespace: metallb-system
spec:
  addresses:
  - 192.168.1.240-192.168.1.250  # Replace with a free IP range on your local network
---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: l2-advert
  namespace: metallb-system
---
: kubectl apply -f metallb-config.yaml


#Install cert-manager
#Install via Helm (most flexible and recommended):

||helm repo add jetstack https://charts.jetstack.io
||helm repo update
||helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --set crds.enabled=true

Apply manifests in the correct order

Access your app securely over HTTPS

🔗 Connect with Me

LinkedIn:https://www.linkedin.com/in/yeyintphyo/ Docker Hub: https://hub.docker.com/repositories/cescye) GitHub: https://github.com/cesscye

This project is a practical demonstration of Kubernetes app deployment, TLS with internal CA, and service exposure using Ingress and MetalLB. Great for learning internal cluster networking and security setups.

