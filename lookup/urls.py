from django.urls import path
from . import views

# We can "include" urls from other APPS in our project in this file 

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
]
