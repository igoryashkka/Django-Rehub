"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from hardware_staff.views import *
from rest_framework import routers
from women.views import pageNotFound
from base import settings

urlpatterns = [
    #path('', include('django_prometheus.urls')),
    #path('', index, name = 'home'),
    path('women/',include('women.urls')),
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('shop-default/',include('shop.urls')),
    path('hardware_staff/', include('hardware_staff.urls')),
    path('api/v1/hardware/',HardwareListAPIView.as_view()),
    path('api/v1/hardware/<int:pk>/',HardwareUpdateAPIView.as_view()),
    path('api/v1/hardware_delete/<int:pk>/',HardwareDestroyAPI.as_view()),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('django_prometheus.urls')),
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound