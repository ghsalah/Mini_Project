from django.db import models
from django.contrib.auth.models import User
import os


    
# ****************************************************************************

def get_profile_pic_upload_path(instance, filename):
    file_extension = filename.split('.')[-1]
    return f'profile_pics/{instance.user.username}.{file_extension}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    profile_pic = models.ImageField(upload_to=get_profile_pic_upload_path, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.pk:  # Check if the object already exists
            old_profile = UserProfile.objects.get(pk=self.pk)
            if old_profile.profile_pic != self.profile_pic:
                if old_profile.profile_pic and os.path.isfile(old_profile.profile_pic.path):
                    os.remove(old_profile.profile_pic.path)

        super(UserProfile, self).save(*args, **kwargs)




def post_upload_path(instance, filename):
    file_extension = filename.split('.')[-1]
    
    # Use instance.pk if available, fallback to count-based logic if not saved yet
    if instance.pk:
        post_id = instance.pk  # Use primary key if the instance is already saved
    else:
        post_id = ImagePost.objects.filter(user=instance.user).count() + 1
    
    return f'posts/{instance.user.username}_post_{post_id}.{file_extension}'

class ImagePost(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link post to user
    image = models.ImageField(upload_to=post_upload_path, blank=True, null=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ===========================================================================================



class JobPost(models.Model):
    job_title = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    experience = models.PositiveIntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Foreign key to UserProfile

    def __str__(self):
        return self.job_title


