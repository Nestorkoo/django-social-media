
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.mainpage, name='home'),
    path('addpost/', views.addpost, name='addpost'),
    
    
]
