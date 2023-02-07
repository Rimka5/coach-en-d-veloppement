from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView


def home (request):
    return render(request, 'coach_rdv/home.html')

def login (request):
    return render(request, 'coach_rdv/login.html')

class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True