"""
Definition of models.
"""

from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField

# Create your models here.

#Category Model/Class
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=32)
    coverImage = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
#Photo Model/Class
class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        )
    datePosted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
#Vidio Model/Class
class Video(models.Model):
    title = models.CharField(max_length=50)
    videoURL = EmbedVideoField()
    category = models.CharField(max_length=50)
    datePosted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
# Photo collection or Album model/class
class photoCollection(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        )
    photos = [models.ImageField(blank=True, null=True)]

    def __str__(self):
        return self.title

# Change background from admin site
class homePageBackground(models.Model):
    backgroundImage = models.ImageField()

# Change About us description from admin site
class AboutUs(models.Model):
    aboutUs = models.TextField()

# Change Video(drone footage) page description from admin site
class DroneDescription(models.Model):
    description = models.TextField()

# Contact info model/class
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
