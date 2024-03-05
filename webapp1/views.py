from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from flask import redirect
from . models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def createpost(request):
    if request.method == "POST":
        new_post = PostForm(request.POST)
        if new_post.is_valid():
            new_post.save()
    post_form = PostForm()
    return render(request, 'createpost.html', {'post_form': post_form})

def signin(request):
    return render(request, 'signin.html')

def posts(request):
    countpost = 10
    page = request.GET.get('page')
    page = int(page)
    posts_all = Post.objects.all()
    posts = posts_all[countpost * (page - 1):countpost * page]
    totalpage = ceil (len(posts_all)/countpost)
    return render(request, 'posts.html', {'posts': posts, 'next_page': page + 1, 'prev_page': page - 1, 'totalpage': totalpage})

def post(request):
    id = request.GET.get('id')
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post, 'id': id})

def deletepost(request):
    id = request.GET.get('id')
    try:
        post = Post.objects.get(id=id)
        if post:
            post.delete()
            return render(request, 'deletepost.html', {'remove': True})
    except Exception:
        return render(request, 'deletepost.html', {'remove': False})

def editpost(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        new_post = PostForm(request.POST, instance=post)
        if new_post.is_valid():
            new_post.save()
            print(1)
        return render(request, 'post.html', {'post': post, 'id': id})
    else:
        new_post = PostForm(instance=post)
        print(2)
        return render(request, 'editpost.html', {'post_form': new_post})