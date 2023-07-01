# Google App Engine Settings

import os
from .settings import *
from google.cloud import secretmanager

DEBUG = False

google_project_id = os.getenv('GOOGLE_PROJECT_ID')
google_secret_name = "django-voyager-secret-key"
parent = f"projects/{google_project_id}"

# Create a Secret Manager client
client = secretmanager.SecretManagerServiceClient()

# Retrieve the secret value
name = f"projects/{google_project_id}/secrets/{google_secret_name}/versions/latest"
response = client.access_secret_version(request={"name": name})
secret_value = response.payload.data.decode("UTF-8")

# Set the secret key in your Django settings
SECRET_KEY = os.getenv('django-voyager-secret-key')

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}