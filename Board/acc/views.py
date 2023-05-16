from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.decorators import login_required


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
