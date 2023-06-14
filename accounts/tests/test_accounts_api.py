import pytest
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

User = get_user_model()

@pytest.mark.django_db
def test_user_registration_api():
    client = APIClient()
    url = '/api/register/'

    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword",
    }

    response = client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert "tokens" in response.data
    assert "refresh" in response.data["tokens"]
    assert "access" in response.data["tokens"]
    assert "testuser" == response.data["username"]
    assert User.objects.filter(username="testuser").exists()

@pytest.mark.django_db
def test_user_login_api(client):
    user = User.objects.create(email='test@example.com')
    user.set_password('testpassword')
    user.save()
    url = '/api/login/'
    data = {
        'email': 'test@example.com',
        'password': 'testpassword',
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'tokens' in response.data

from rest_framework.test import APIClient

@pytest.mark.django_db
def test_user_api():
    client = APIClient()
    user = User.objects.create(email='test@example.com')
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token.access_token))
    url = '/api/user/'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'email' in response.data
