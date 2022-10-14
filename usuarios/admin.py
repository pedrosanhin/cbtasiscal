"""Usuarios admin classes."""

# Django
from django.contrib import admin

# Models
from usuarios.models import Maestro, Alumno, Grupo

admin.site.register(Grupo)
admin.site.register(Maestro)
admin.site.register(Alumno)