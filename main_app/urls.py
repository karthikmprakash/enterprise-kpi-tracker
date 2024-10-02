from django.urls import include, path

from . import views

urlpatterns = [
    # path("", views.check_authentication, name="check_authentication"),
    path("", include("social_django.urls")),
    path("", views.home, name="home"),
    path("logout", views.logout, name="logout"),
]
