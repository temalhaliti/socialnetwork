from multiprocessing import context
from .forms import PostForm
from django.shortcuts import render
from .models import Profile
from django.shortcuts import render, redirect

def base(request):
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("social:base")
    form = PostForm()
    context = {"form": form}
    return render(request, "dashboard.html", context)

def profilelist(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {"profiles": profiles}
    return render(request, "profilelist.html", context)

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
        
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    context = {"profile": profile}
    return render(request, "profile.html", context)
