from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts import views

app_name = "users"

urlpatterns = [
    path("api/register/", views.UserRegisterationAPIView.as_view(), name="create-user"),
    path("api/login/", views.UserLoginAPIView.as_view(), name="login-user"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("api/user/", views.UserAPIView.as_view(), name="user-info"),
]
