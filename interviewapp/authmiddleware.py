import base64
import requests
from django.contrib.auth import authenticate
from django.http import HttpResponseForbidden

#OPA_URL = 'http://127.0.0.1:57918/v1/data/admin'
OPA_URL = 'http://opa:8181/v1/data/admin'
class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        auth_header = request.headers.get('Authorization')

        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Basic '):
            try:
                # Decode the Base64-encoded credentials
                credentials = auth_header.split(' ')[1].encode('utf-8')
                decoded_credentials = base64.b64decode(credentials).decode('utf-8')
                username, password = decoded_credentials.split(':')
                user = authenticate(request, username=username, password=password)
                if request.method == 'POST':
                    payload = {"input": {"user": {"is_superuser": user.is_superuser}}}
                    response = requests.post(OPA_URL, json=payload)
                    if not response.json()['result']['allow']:
                        return HttpResponseForbidden("Only admins allowed to create a user")
            except Exception as e:
                pass

        response = self.get_response(request)
        return response