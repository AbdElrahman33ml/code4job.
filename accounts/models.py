from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class City(models.Model):
    name=models.CharField(max_length=30)
def __str__(self):
    return self.name


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    city=models.ForeignKey('City', on_delete=models.CASCADE,blank=True,null=True)
    phone=models.CharField( max_length=15)
    image=models.ImageField(upload_to='profile/')


def __str__(self):
     return self.name

#once create user a new empty profile create throgh below function

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)





