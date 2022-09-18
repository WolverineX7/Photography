from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login), 
    path('signup',views.signup),
    path('about',views.about),
    path('portfolio',views.portfolio),
    path('',views.home),
    path('index',views.home),
    path('contact',views.contact),
    path('login/signup',views.index),
]
