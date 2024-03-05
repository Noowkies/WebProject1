from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('webapp1/', views.index, name='index'),
    path('webapp1/home', views.home, name='home'),
    path('webapp1/signin', views.signin, name='signin'),
    path('webapp1/createpost', views.createpost, name='createpost'),
    path('webapp1/posts', views.posts, name='posts'),
    path('webapp1/post', views.post, name='post'),
    path('webapp1/deletepost', views.deletepost, name='delete'),
    path('webapp1/post/<int:id>/edit', views.editpost, name='edit'),
]