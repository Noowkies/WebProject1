from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('webapp1/', views.index, name='index'),
]