"""cbtasiscal URL Configuration"""

# Django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('usuarios/', include(('usuarios.urls', 'urls'), namespace='usuarios')),
]
