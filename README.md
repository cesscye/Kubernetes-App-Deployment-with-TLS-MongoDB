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

📂 File Structure

├── app.py
├── Dockerfile
├── k8s/
│   ├── flask-deployment.yaml
│   ├── flask-service.yaml
│   ├── mongo-statefulset.yaml
│   ├── mongo-headless-service.yaml
│   ├── ingress.yaml
│   ├── cert-manager/
│   │   ├── cluster-issuer.yaml
│   │   ├── certificate.yaml
│   └── metallb-config.yaml

🧪 Try It Yourself

Deploy NGINX Ingress Controller

Install MetalLB and configure IP pool

Install cert-manager

Apply manifests in the correct order

Access your app securely over HTTPS

🔗 Connect with Me

LinkedIn: [your-linkedin-profile]Docker Hub: [your-dockerhub-link]GitHub: [your-repo-link]

This project is a practical demonstration of Kubernetes app deployment, TLS with internal CA, and service exposure using Ingress and MetalLB. Great for learning internal cluster networking and security setups.

