from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('read_post/<str:id>/<str:slug>/', views.read_post, name='read_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('share_post/<str:id>/', views.share_post, name='share_post'),
    path('update_post/<str:id>/', views.update_post, name='update_post'),
    path('delete_post/<str:id>/', views.delete_post, name='delete_post'),
    path('delete_comment/<str:id>/', views.delete_comment, name='delete_comment'),
    path('update_comment/<str:id>/', views.update_comment, name='update_comment'),
    path('posts/<str:category>/', views.post_categories, name='post_categories'),

]
