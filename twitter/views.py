from django.shortcuts import render, redirect
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
                return HttpResponse("Invalid username or password")
    else:
        user_signin = LoginForm()
        return render(request,'twitter/signin.html',{"user_signin":user_signin})

def signout(request):
    logout(request)
    return redirect("twitter:home")




