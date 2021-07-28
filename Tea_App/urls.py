from django.conf.urls import url
from django.urls import path
from Tea_App import views

app_name = 'Tea_App'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blog-details/<int:pk>/', views.blog_details, name="blog_details"),
    path('blog/', views.blog, name="blog"),
    # path('help/', views.c, name="help"),
    path('tea_details/<int:id>/', views.tea_details, name="tea_details"),
    path('types/', views.types, name="types"),
    path('help', views.Contact.as_view(), name='help'),
    path('search/',views.search,name='search'),
    path('black_tea/', views.black_tea, name='black_tea'),
    path('green_tea/', views.green_tea, name='green_tea'),
    path('white_tea/', views.white_tea, name='white_tea'),
    path('matcha_tea/', views.matcha_tea, name='matcha_tea'),
    path('oolong_tea/', views.oolong_tea, name='oolong_tea'),
    path('fermented_tea/', views.fermented_tea, name='fermented_tea'),
    path('herbal_tea/', views.herbal_tea, name='herbal_tea'),

]
