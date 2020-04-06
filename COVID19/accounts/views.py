# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import views
from . import forms

# Create your views here.
class SignUp(CreateView):
	form_class  = forms.UserCreateForm
	success_url = reverse_lazy('accounts:login')
	template_name = 'accounts/signup.html'

class LoginView(views.LoginView):
	form_class = forms.LoginForm
	success_url = reverse_lazy('home')
	template_name = 'accounts/login.html'
