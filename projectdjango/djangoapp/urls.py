from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('credential', views.register, name='register'),
    path('login', views.login,name='login'),
    path('about', views.about,name='about'),
    path('education', views.education,name='education'),
    path('blog', views.blog,name='blog'),
    path('college', views.college,name='college'),
    path('contact', views.contact,name='contact'),
]