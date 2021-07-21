from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View
from .models import Blog, SiteUtilities, AboutMe, ImageSlider, Subscribers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def home(request):
    if request.method == "POST":
        subs_mail = request.POST.get('subs_mail')
        subs_first_name = request.POST.get('subs_first_name')

        subscribers = Subscribers.objects.all()
        match = False

        for subscribers in subscribers:
            if subs_mail == subscribers.subs_mail:
                match = True

        if match:
            messages.error(request, "You Are Already Subscribed!")
        else:
            subs_ins = Subscribers(subs_mail = subs_mail, subs_first_name = subs_first_name)
            subs_ins.save()
            messages.success(request, "Subscription Added Successfully!")


    image_slider = ImageSlider.objects.all()
    about_me = AboutMe.objects.all()
    site_utils = SiteUtilities.objects.all()
    dict = {'about_me' : about_me, 'img_slider' : image_slider, 'site_utils' : site_utils}
    return render(request, 'Tea_App/index.html', dict)

def about(request):
    site_utils = SiteUtilities.objects.all()
    dict = {'site_utils' : site_utils}
    return render(request, 'Tea_App/about.html', dict)

def blog_details(request, pk):
    blog1 = Blog.objects.order_by('-published_date')
    blog = Blog.objects.get(id=pk)
    dict = {'blog': blog, 'recent_blogs' : blog1}
    return render(request, 'Tea_App/blog-details.html', dict)

def blog(request):
    blog = Blog.objects.order_by('-published_date')
    paginator = Paginator(blog, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    dict = {'blog' : paged_blogs, 'recent_blogs' : blog}
    return render(request, 'Tea_App/blog.html', dict)

def help(request):
    site_utils = SiteUtilities.objects.all()
    dict = {'site_utils' : site_utils}
    return render(request, 'Tea_App/help.html', dict)

def tea_details(request):
    return render(request, 'Tea_App/tea-details.html')

def types(request):
    return render(request, 'Tea_App/types.html')