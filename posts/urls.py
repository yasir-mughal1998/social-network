from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, LikePostAPIView

app_name = "posts"

router = DefaultRouter()
router.register("api/posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api/posts/<int:pk>/like/', LikePostAPIView.as_view(), name='like_post'),
]
