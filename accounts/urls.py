from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/<str:username>/<str:id>/', views.user_profile, name='profile'),
    path('update_profile/<str:username>/<str:id>/', views.update_profile, name='update_profile'),
]
