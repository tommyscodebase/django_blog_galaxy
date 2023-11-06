from django.shortcuts import redirect, render
from django.db.models import Q
from accounts.models import UserProfile
from base.forms import CommentForm, EmailPostForm, PostForm
from .models import Category, Comment, Post
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.text import slugify
from django.core.mail import send_mail

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
    
# Create a Post
def create_post(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.user
        body = request.POST.get('body')
        category = request.POST.get('category')
        try:
            image = request.FILES['post-image']
        except MultiValueDictKeyError:
            image = None
        
        slug = slugify(title)

        post = Post(
            author=author,
            title=title,
            slug=slug,
            body=body,
            image=image,
            category=category,
        )
        post.save()
        return redirect('home')
    return render(request, 'create_post.html', {
        'categories':categories,
    })

# Read a post
def read_post(request, id, slug):
    post = Post.objects.get(id=id, slug=slug)
    similar_posts = Post.objects.filter(category=post.category)
    post_comments = Comment.objects.filter(c_post=post)

    if request.method == 'POST':
        author = request.POST.get('name')
        body = request.POST.get('comment')
        if request.user.is_authenticated:
            new_comment = Comment(
                author=author,
                c_post=post,
                body=body,
                registered_user=request.user,
            )
        else:
            new_comment = Comment(
                author=author,
                c_post=post,
                body=body,
            )
        new_comment.save()

    return render(request, 'post.html', {
        'post': post,
        'similar_posts': similar_posts,
        'post_comments': post_comments,
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

# Delete Comment
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        post = comment.c_post
        post_url = post.get_absolute_url()
        comment.delete()
        return redirect(post_url)
    return render(request, 'delete.html',{
         'item':comment,
        'type': 'comment',
    })



# Update Comment
def update_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        post = comment.c_post
        post_url = post.get_absolute_url()
        return redirect(post_url)
    else:
       form = CommentForm(instance=comment) 
    return render(request, 'update_comment.html',{
         'form':form,
        'comment': comment,
    })


# Share Post
def share_post(request, id):
    post = Post.objects.get(id=id)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends that you read {post.title}"
            message = f"Read this post I found on Galaxy. The url is {post_url} and the title is {post.title}. {cd['name']} gave the comment below {cd['comments']}"

            send_mail(
                subject=subject,
                message=message,
                from_email=request.user.email,
                recipient_list=[cd['to']]
            )
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'share_post.html', {
        'post': post,
        'form': form,
        'sent': sent
    })