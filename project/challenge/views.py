from django.shortcuts import render

# Create your views here.

def idea(request):
    return render(request, 'idea.html')

def travel(request):
    return render(request, 'travel.html')

def fun(request):
    return render(request, 'fun.html')