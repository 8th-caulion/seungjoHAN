from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def actor(request):
    return render(request, 'actor.html')