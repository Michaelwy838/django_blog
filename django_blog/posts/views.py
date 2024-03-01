from django.shortcuts import render
from .models import Post

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render (request, 'posts/posts_list.html', {'posts': posts})

def single_post(request, slug):
    post = Post.objects.get(slug = slug)
    return render (request, 'posts/single_post.html', {'post': post})

def my_posts(request, author):
    myposts = Post.objects.get(author = author)
    return render (request, 'posts/myposts.html', {'myposts': myposts})