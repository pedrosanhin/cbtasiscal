from django.contrib import admin

from .models import Materia, Grupo, Semestre

# Register your models here.

admin.site.register(Materia)
admin.site.register(Grupo)
admin.site.register(Semestre)
