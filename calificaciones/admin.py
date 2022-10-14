from django.contrib import admin

from .models import Calificaciones, Materia, Semestre

# Register your models here.

admin.site.register(Materia)
admin.site.register(Semestre)
admin.site.register(Calificaciones)
