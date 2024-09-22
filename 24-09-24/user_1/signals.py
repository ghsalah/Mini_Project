from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Only create a UserProfile if it doesn't already exist
        UserProfile.objects.get_or_create(user=instance)
    else:
        # If the user profile exists, update it
        instance.userprofile.save()
