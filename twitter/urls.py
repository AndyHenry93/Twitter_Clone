from django.urls import path
from . import views

app_name = "twitter"

urlpatterns = [
    path('',views.home,name='home'),
    path('profile_list/',views.profile_list,name='profile_list'),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout")
]