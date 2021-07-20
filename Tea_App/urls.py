from django.conf.urls import url
from django.urls import path
from Tea_App import views

app_name='Tea_App'

urlpatterns = [
    path('',views.index,name='index'),

]