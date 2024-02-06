from django.urls import path 
from .views import *
from . import views


urlpatterns = [
    path('',WomenHome.as_view(), name = 'home'),
    path('about/',views.about,name = 'about'),
    path('show_post/<slug:slug>',ShowPost.as_view(),name='post'),
    path('show_cat/<int:cat_id>',ShowCategory.as_view(),name='cat'),
    path('cat/<int:catid>/',views.cat),
    path('addpage',AddPage.as_view(),name='addpage'),
    path('show_cat/addpage',AddPage.as_view(),name='addpage'),#Kostulь?
    path('register/',RegisterUser.as_view(),name = 'register'),
    path('login/',LoginUser.as_view(),name = 'login'),
    path('logout/',logout_user,name = 'logout')
]

