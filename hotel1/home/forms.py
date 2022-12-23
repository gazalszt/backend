from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

class signupform(UserCreationForm):
    email =forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
