from django.shortcuts import render

# Create your views here.

def season1(request):
    return render(request, 'season1.html')

def season2(request):
    return render(request, 'season2.html')
