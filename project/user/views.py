from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from user.models import User


class AuthView(CreateView):
    model = User
    fields = ["username", "email", "password"]