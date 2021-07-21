from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class SiteUtilities(models.Model):
    about_us_avatar = models.ImageField(upload_to = 'site_utilities')
    about_us_description = RichTextField()
    help_text = RichTextField()

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    blog = RichTextField()
    thumbnail_img = models.ImageField(upload_to = 'blog_thumbnails')
    published_date = models.DateTimeField(default=datetime.now(), blank=True)

class Subscribers(models.Model):
    subs_mail = models.EmailField(max_length=300)
    subs_first_name = models.CharField(max_length=300)

class AboutMe(models.Model):
    about_me_avatar = models.ImageField(upload_to = 'about_me_picture')
    about_me_description = RichTextField()

class ImageSlider(models.Model):
    slider_img = models.ImageField(upload_to = 'slider_images')
    active = models.BooleanField(default=False)
