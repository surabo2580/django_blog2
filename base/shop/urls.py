from django.contrib import admin
from django.urls import path
from feeds import views

urlpatterns = [
    
    path('',views.homeFeed,name='feedHome'),
    path('<str:slug>',views.feedPost,name='feedPost'),
]
