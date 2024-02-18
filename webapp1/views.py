from django.http import HttpResponse
from django.shortcuts import render
from . models import Post

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def firstpost(request):
    post = Post.objects.get(id=1)
    return render(request, 'firstpost.html', {'firstpost': post})

def secondpost(request):
    post = Post.objects.get(id=2)
    return render(request, 'secondpost.html', {'secondpost': post})

def signin(request):
    return render(request, 'signin.html')
