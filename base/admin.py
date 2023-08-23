from django.contrib import admin
from .models import Category, Comment, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}