from django.shortcuts import redirect, render
from django.db.models import Q
from accounts.models import UserProfile
from base.forms import PostForm
from .models import Category, Post

# Create your views here.
# Homepage
def post_categories(request, category):
    posts = Post.objects.filter(category=category)
    recent_posts = Post.objects.all()[0:5]
    existing_categories = Category.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
        'recent_posts': recent_posts,
        'existing_categories': existing_categories,
        })


def home(request):
    if request.user.is_authenticated:
        filter_query = request.GET.get('q') if request.GET.get('q') != None else ''
        # Search Engine
        posts = Post.objects.filter(
            Q(title__icontains=filter_query) |
            Q(author__username__icontains=filter_query) |
            Q(category__icontains=filter_query) 
        )

        profile = UserProfile.objects.get(person=request.user)
        existing_categories = Category.objects.all()
        recent_posts = Post.objects.all()[0:5]
        return render(request, 'index.html', {
            'posts': posts,
            'recent_posts': recent_posts,
            'profile': profile,
            'existing_categories': existing_categories,
        })
    else:
        filter_query = request.GET.get('q') if request.GET.get('q') != None else ''
        # Search Engine
        posts = Post.objects.filter(
            Q(title__icontains=filter_query) |
            Q(author__username__icontains=filter_query) |
            Q(category__icontains=filter_query) 
        )
        existing_categories = Category.objects.all()
        recent_posts = Post.objects.all()[0:5]
        return render(request, 'index.html', {
            'posts': posts,
            'recent_posts': recent_posts,
            'existing_categories': existing_categories,
        })

# Read a post
def read_post(request, id, slug):
    post = Post.objects.get(id=id, slug=slug)
    similar_posts = Post.objects.filter(category=post.category)
    return render(request, 'post.html', {
        'post': post,
        'similar_posts': similar_posts,
    })

# Update Post
def update_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile', username=post.author.username, id=post.author.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'update_post.html', {
        'form':form,
        'post':post,
    })

# Delete Post
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('profile', username=post.author.username, id=post.author.id)
    return render(request, 'delete.html', {
        'item':post,
        'type': 'post',
    })