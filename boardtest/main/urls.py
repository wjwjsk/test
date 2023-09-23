from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("article_create/", views.article_create, name="article_create"),
    path("login/", views.login_view, name="login"),
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("register/", views.register_view, name="register"),
    path("social_login/", views.social_login_view, name="social_login"),
]
