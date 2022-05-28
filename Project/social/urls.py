from django.urls import path
from .views import base, profilelist, profile

app_name = "social"

urlpatterns = [
    path("", base, name="base"),
    path("profilelist/", profilelist, name="profilelist"),
    path("profile/<int:pk>", profile, name="profile"),
]