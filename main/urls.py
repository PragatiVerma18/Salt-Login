from django.urls import path
from main.views import homepage, register_request, login_request, logout_request

app_name = "main"

urlpatterns = [
    path("", homepage, name="homepage"),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),
]
