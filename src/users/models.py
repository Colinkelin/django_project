from django.db import models
from django.contrib.auth.models import User

#from localflavor.cn.cn_provinces import CN_PROVINCE_CHOICES
from localflavor.us.models import USStateField

class Location(models.Model):
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=64)
   #province = CN_PROVINCE_CHOICES()
    state = USStateField(default="WA")

    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
#one user can only have one profile vice versa. Creates a relatonship between the user and the profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#if user model gets delete then the profile model will also get deleted
    photo =  models.ImageField(upload_to='main/pics')
    bio = models.CharField(max_length=160, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
#location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
#dont set models to CASCADE because if the location gets deleted then the corresponding profile will be deleted too. 
#create the migrations and apply migrations to the database after making changes to the models.py
    def __str__(self): 
        return f'{self.user.username}\'s Profile'




# Create your models here.