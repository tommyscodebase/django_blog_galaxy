from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    about = models.TextField()
    talks_about = models.CharField(max_length=200, default='anything')
    avatar = models.ImageField(upload_to='profile_photos', default='user.jpg')
    
    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url

    def __str__(self):
        return f'Profile of {self.person.first_name} {self.person.last_name}'
