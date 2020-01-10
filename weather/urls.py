from django.contrib import admin
from django.urls import path, include

# We can "include" urls from other APPS in our project in this file 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lookup.urls')),
]