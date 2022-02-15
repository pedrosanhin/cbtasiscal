"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    """
    Usuario model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    es_alumno = models.BooleanField('alumno status', default=False)
    es_maestro = models.BooleanField('maestro status', default=False)
    