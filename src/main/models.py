from django.db import models
import uuid
from users.models import Profile, Location
from .car_brands import CAR_BRANDS, TRANSMISSION_OPTIONS

class Listing(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)#creating unique listingid
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')#one to many relationship(one owner can make multiple listings) .CASCADE so that when the user gets deleted then the listings tied to him also get deleted
    brand = models.CharField(max_length=20, choices=CAR_BRANDS, default=None) #choices listed in car_brands.py
    model = models.CharField(max_length=64)
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=24)
    description = models.TextField()
    engine = models.CharField(max_length=30)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_OPTIONS, default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    #a listing can only be linked to a particular location. only location gets deleted upon delete
    image = models.ImageField(upload_to='main/pics', null=True)
    profile_picture = models.ImageField(upload_to='main/pics', null=True)

    def __str__(self):
        return f'{self.owner.user.username}\'s Listing - {self.brand} {self.model}'

    def getowner_photo(self):
        profile_picture = self.owner.photo

    def save(self, *args, **kwargs):
        self.getowner_photo()        
        super(Listing, self).save(*args, **kwargs)
        
# Create your models here.
