# Kubernates and OPA policy test Project 
- Install latest version of  minikube, docker on to your local computer 
- Clone this project on your local machine 


## Project setup instruction 
### Prerequisites 
- Ensure docker and minikube are running 

### Setup Instructions
- Inside the project root, build the docker image `docker build -t app .`
- Load this docker image into minikube `minikube image load app:latest`
- Apply kubernates configs your cluster `kubectl apply -f deploy/deployment.yaml`

### Setup Opa Service
- Create configMap for out policys `kubectl create configmap example-policy --from-file deploy/policy.rego`
- Apply Opa configs on your cluster `kubectl apply -f deploy/opa-deployment.yaml`

### Create an Admin User
- Check for a pot to user `kubectl get pods`
- Create a Admin  to interact with the API `kubectl exec -it your-pod-name -- python manage.py createsuperuser --stdin`

### Generate service  URL for your cluster 
- Get the service URL for your kubernates cluster `minikube service userapi-service --url`

## API Documentation interaction

### Get users
- User the service url get list of users : `http://{{SERVICE_URL}}/users/`
- Create User the service url, send a post requet : `http://{{SERVICE_URL}}/users/`
- Sample Post payload 
  ```
  {
    "name": "Ian normal example",
    "email": "ian@example.com",
    "password": "",
    "is_superuser": True/False
   }
   ```
- API user basic Auth for authetication 
- Only supersers/admin can create users
- API documentation at `http://{{SERVICE_URL}}/users/`
