from django.http import HttpResponse
from django.shortcuts import render
from . models import Post
from .forms import PostForm

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

def createpost(request):
    if request.method == "POST":
        new_post = PostForm(request.POST)
        if new_post.is_valid():
            new_post.save()
    post_form = PostForm()
    return render(request, 'createpost.html', {'post_form': post_form})

def signin(request):
    return render(request, 'signin.html')
