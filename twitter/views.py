from django.shortcuts import render, redirect, get_object_or_404
from . models import Profile
from . forms import LoginForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'twitter/home.html')

def profile_list(request):
    profile = Profile.objects.exclude(user=request.user)
    context = {
        "profiles":profile
    }
    return render(request,'twitter/profile_list.html',context)

def signin(request):
    if request.method == 'POST':
        user_signin = LoginForm(request.POST)
        if user_signin.is_valid():
            cd = user_signin.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                return redirect('twitter:home')
            else:
                messages.error(request,"Invalid username or password, Please try again.")
                return redirect("twitter:home")
    else:
        user_signin = LoginForm()
        return render(request,'twitter/signin.html',{"user_signin":user_signin})

def signout(request):
    logout(request)
    return redirect("twitter:home")

def profile(request,id):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile,id=id)
        # form logic
        if request.method == "POST":
            # get current user
            curr_user = request.user.profile
            # get form data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == "unfollow":
                curr_user.follow.remove(user_profile)
            else:
                curr_user.follow.add(user_profile)
            curr_user.save()
        context = {
            "user_profile":user_profile
        }
        return render(request,'twitter/profile.html',context)
    else:
        messages.error(request,"you must be logged in to access this page")
        return redirect("twitter:home")





