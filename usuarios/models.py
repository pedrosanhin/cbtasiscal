"""Users models."""

# Django
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models

class Alumno(models.Model):
    """
    Alumno model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.user.first_name} {self.user.last_name}')

class Maestro(models.Model):
    """
    Maestro model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    CIUDADANO = 'C'
    TECNICO = 'TEC'
    LICENCIATURA = 'LIC'
    INGENIERIA = 'ING'
    MAESTRIA = 'MT'
    DOCTORADO = 'DOC'

    G_E = [
        (CIUDADANO, 'Ciudadano'),
        (TECNICO, 'Técnico'),
        (LICENCIATURA, 'Licenciatura'),
        (INGENIERIA, 'Ingeniería'),
        (MAESTRIA, 'Maestría'),
        (DOCTORADO, 'Doctorado'),
    ]

    grado_de_estudios = models.CharField(
        max_length=3,
        choices=G_E,
        default=LICENCIATURA)

    def __str__(self):
        return (f'{self.grado_de_estudios} {self.user.first_name} {self.user.last_name}')