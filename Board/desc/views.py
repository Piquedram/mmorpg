from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Category, Post


class BaseView(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostsView(BaseView, ListView):
    model = Post
    ordering = '-created'
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostsCatView(PostsView):
    template_name = 'category.html'


class PostView(BaseView, DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class CategoriesView(BaseView, ListView):
    model = Category
    ordering = 'id'
    template_name = 'categories.html'
    context_object_name = 'categories'


def media_display_view(request):
    post = Post.objects.all()[2]  # Получаем первый пост, можно настроить выборку по вашей логике
    html_code_from_ckeditor = post.text

    return render(request, 'media_display.html', {'html_code': html_code_from_ckeditor})
