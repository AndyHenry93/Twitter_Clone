from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Unregister Group and initial user
admin.site.unregister(Group)
admin.site.unregister(User)

# mix profile info into user info 
class ProfileInline(admin.StackedInline):
    model = Profile 

# extend user model 
class UserAdmin(admin.ModelAdmin):
    model = User 
    fields = ['username']
    inlines = [ProfileInline]

# Reregister new user model
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

