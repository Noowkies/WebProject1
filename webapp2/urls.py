from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('webapp2/', views.test, name='test'),
]