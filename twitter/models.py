from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.dispatch import receiver

# user profile model 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follow = models.ManyToManyField("self",related_name="followed_by",symmetrical=False,blank=True)
    updated = models.DateTimeField(User,auto_now=True)
    img = models.ImageField(default="static/img/icon.png",blank=True,upload_to="media/%Y/%M/profile_img/")


    def __str__(self):
        return self.user.username
    
# create profile when new user signs up 
@receiver(post_save, sender = User)
def create_profile(instance,created,**kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # have the user follow themselves 
        user_profile.follow.set([instance.profile.id])
        user_profile.save()
