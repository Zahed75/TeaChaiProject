from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View
# Create your views here.

def index(request):
    return HttpResponse("Hello")