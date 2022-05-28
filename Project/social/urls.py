from django.urls import path
from .views import base, profilelist

app_name = "social"

urlpatterns = [
    path("", base, name="base"),
    path("profilelist/", profilelist, name="profilelist"),
]