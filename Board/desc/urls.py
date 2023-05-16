from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import PostsView, PostView, PostsCatView, CategoriesView, media_display_view


urlpatterns = [
    path('posts/', PostsView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', PostView.as_view(), name='post_detail'),
    path('categories/', CategoriesView.as_view(), name='categories_list'),
    path('categories/<int:pk>/', PostsCatView.as_view(), name='category_detail'),
    path('test/', media_display_view, name='media_display'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
