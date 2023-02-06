from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    # HttpResponse('<h1>Hello Django !</h1>')

    return render(request, 'coach_rdv/home.html')
