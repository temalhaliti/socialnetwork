from django.urls import path
from .views import base

app_name = "social"

urlpatterns = [
    path("", base, name="base"),
]