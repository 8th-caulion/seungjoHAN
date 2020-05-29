from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('local1.urls')),
    path('season/', include('local2.urls')),
]
