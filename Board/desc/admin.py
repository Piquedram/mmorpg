from django.contrib import admin

from .models import Category, Post
from .forms import PostAdmin


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
