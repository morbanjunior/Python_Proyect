from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE,
        primary_key=True,)
    description = models.CharField(max_length = 100, default = '')
    city = models.CharField(max_length = 100, default = '')
    website = models.URLField(default = '')
    phone = models.URLField(default = 0)

def Create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(User = kwargs['instance'])

post_save.connect(Create_profile, sender=User)


        