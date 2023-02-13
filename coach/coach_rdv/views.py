from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.http import HttpResponse

def home (request):
    return render(request, 'coach_rdv/home.html')

def registre (request):
    if request.method == "poste":
        username = request.Post['username']
        email = request.Post['email']
        password1 = request.Post['password1']
        password2 = request.Post['password2']
        mon_utilisateur = User.objects.create_user(username, email, password1)
        mon_utilisateur.username = username
        mon_utilisateur.save()
        messages.success(request, 'votre compte a bien été crée avec succès')
        return redirect('login')
        
        
    return render(request, 'coach_rdv/registre.html')


def login (request):
    if request.method == "poste":
        username = request.Post['username']
        password1 = request.Post['password1']
        user = authenticate(username=username, password1=password1)
        if user is not None:
            login(request, user)
            username = user.username
            return render(request, 'coach_rdv/home.html', {'username':username})
        else:
            messages.error(request, 'le site n a pas pu vous authentifier')
            return redirect ('login')
    return render(request, 'coach_rdv/login.html')

def logout (request):
    pass
class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True