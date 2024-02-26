from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('webapp1/', views.index, name='index'),
    path('webapp1/firstpost', views.firstpost, name='firstpost'),
    path('webapp1/secondpost', views.secondpost, name='secondpost'),
    path('webapp1/home', views.home, name='home'),
    path('webapp1/signin', views.signin, name='signin'),
    path('webapp1/createpost', views.createpost, name='createpost')
]