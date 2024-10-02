from django.urls import include, path

from . import views

urlpatterns = [
    path("", view=include("social_django.urls")),
    path("", view=views.home, name="home"),
    path("login", view=views.login, name="login"),
    path("logout", view=views.logout, name="logout"),
    path("dashboard", view=views.dashboard, name="dashboard"),
    path("login/auth0", view=views.callback, name="callback"),
]
