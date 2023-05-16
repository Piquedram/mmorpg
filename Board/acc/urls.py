from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView

from .views import ProfileView

urlpatterns = [
    path('', login_required(ProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
]
