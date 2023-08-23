from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('read_post/<str:id>/<str:slug>/', views.read_post, name='read_post'),
    path('update_post/<str:id>/', views.update_post, name='update_post'),
    path('delete_post/<str:id>/', views.delete_post, name='delete_post'),
    path('posts/<str:category>/', views.post_categories, name='post_categories'),

]
