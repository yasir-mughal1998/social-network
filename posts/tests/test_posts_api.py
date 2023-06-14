import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from posts.models import Post
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


@pytest.mark.django_db
class TestPostViewSet:
    def test_list_posts(self):
        client = APIClient()
        url = "/api/posts/"

        user = User.objects.create(email='test@example.com')

        Post.objects.create(
            title="Post 1", body="body 1", author=user)
        Post.objects.create(
            title="Post 2", body="body 2", author=user)

        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_create_post(self):
        client = APIClient()
        url = "/api/posts/"

        user = User.objects.create(email='test@example.com')
        token = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           str(token.access_token))

        payload = {"title": "New Post", "body": "New body"}
        response = client.post(url, payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED

    def test_retrieve_post(self):
        client = APIClient()

        user = User.objects.create(email='test@example.com')
        token = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           str(token.access_token))

        post = Post.objects.create(
            title="Test Post", body="Test body")

        url = f"/api/posts/{post.id}"

        response = client.get(url, follow=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "Test Post"

    def test_update_post(self):
        client = APIClient()

        user = User.objects.create(email='test@example.com')
        token = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           str(token.access_token))

        post = Post.objects.create(
            title="Test Post", body="Test body")

        url = f"/api/posts/{post.id}"

        payload = {"title": "Updated Post", "body": "Updated body"}

        response = client.put(url, payload, format="json", follow=True)

        assert response.status_code == status.HTTP_200_OK

    def test_destroy_post(self):
        client = APIClient()

        user = User.objects.create(email='test@example.com')
        token = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           str(token.access_token))

        post = Post.objects.create(
            title="Test Post", body="Test body", author=user)

        url = f"/api/posts/{post.id}"

        response = client.delete(url, follow=True)

        assert response.status_code == status.HTTP_200_OK