from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, Location


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_location_profile(sender, instance, created, **kwargs):
    if created:
        #Location.objects.create(profile=instance)
        profile_location = Location.objects.create()
        instance.location = profile_location
        instance.save()