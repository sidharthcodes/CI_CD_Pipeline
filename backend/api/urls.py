from django.urls import path
from . import views

urlpatterns = [
    path("", views.default, name="default"),
    path("health/", views.health, name="health"),
    path("api/echo/", views.echo, name="echo"),
]
