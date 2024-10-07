
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estilo/', include('estilo.urls')),
    path('', include('cantor.urls')),
]