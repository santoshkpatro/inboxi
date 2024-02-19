from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")