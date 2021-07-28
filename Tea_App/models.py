from django.db import models

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from datetime import  timezone


class SiteUtilities(models.Model):
    about_us_avatar = models.ImageField(upload_to = 'site_utilities',verbose_name="Please put your about us profile pic")
    about_us_description = RichTextField()
    help_text = RichTextField()
    home_first_section_heading = RichTextField()
    home_second_section_heading = RichTextField()
    types_heading = RichTextField()

class Subscribers(models.Model):
    subs_mail = models.EmailField(max_length=300)
    subs_first_name = models.CharField(max_length=300)

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    blog = RichTextField()
    thumbnail_img = models.ImageField(upload_to = 'blog_thumbnails')
    published_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Blog)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        subscribers_list = []
        subs = Subscribers.objects.all()

        for subscribers in subs:
            subscribers_list.append(subscribers.subs_mail)

        send_mail(
            "New Post Uploaded",
            "A new post has just been uploaded. Check right now!",
            'drinkteaville@gmail.com',
            subscribers_list,
            fail_silently=False
        )

class AboutMe(models.Model):
    about_me_avatar = models.ImageField(upload_to = 'about_me_picture')
    about_me_description = RichTextField()

class ImageSlider(models.Model):
    slider_img = models.ImageField(upload_to = 'slider_images')
    active = models.BooleanField(default=False)

class TypesOfTea(models.Model):
    tea_picture = models.ImageField(upload_to='tea_types')
    type_name = models.CharField(max_length = 100, null=True)
    tea_description = RichTextField()
    first_section = models.BooleanField(default = False)
    second_section = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add=True)

class Black_tea(models.Model):
    tea_picture = models.ImageField(upload_to='black_tea')
    type_name = models.CharField(max_length=100, null=True)
    tea_description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

class Green_tea(models.Model):
    tea_picture = models.ImageField(upload_to='green_tea')
    type_name = models.CharField(max_length=100, null=True)
    tea_description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)


class White_tea(models.Model):
    tea_picture = models.ImageField(upload_to='white_tea')
    type_name = models.CharField(max_length=100, null=True)
    tea_description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

class Matcha_tea(models.Model):
    tea_picture = models.ImageField(upload_to='matcha_tea')
    type_name = models.CharField(max_length=100, null=True)
    tea_description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

class Oolong_tea(models.Model):
    tea_picture = models.ImageField(upload_to='oolong_tea')
    type_name = models.CharField(max_length=100, null=True)
    tea_description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

class Fermented_tea(models.Model):
    tea_picture = models.ImageField(upload_to='fermented_tea')
    type_name = models.CharField(max_length=100, null=True)
    tea_description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

class Herbal_tea(models.Model):
    tea_picture = models.ImageField(upload_to='herbal_tea')
    type_name = models.CharField(max_length=100, null=True)
    tea_description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)