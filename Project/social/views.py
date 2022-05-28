from multiprocessing import context
from django.shortcuts import render
from .models import Profile

def base(request):
    return render(request, "base.html")

def profilelist(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {"profiles": profiles}
    return render(request, "profilelist.html", context)

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    context = {"profile": profile}
    return render(request, "profile.html", context)
