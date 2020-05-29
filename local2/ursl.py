from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('season1/', views.season1, name = "season1"),
    path('season2/', views.season2, name = "season2"),
]
