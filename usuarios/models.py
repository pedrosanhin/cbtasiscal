"""Users models."""

# Django
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models

class Grupo(models.Model):
    GRUPOS = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]

    GENE = 'GEN'
    OFI = 'OFI'
    SSP = 'SSP'
    SPA = 'SPA'
    AGRO = 'AGRO'
    DS = 'DS'

    CARRERAS = [
        (GENE, 'General'),
        (OFI, 'Ofimática'),
        (SSP, 'Sistemas de Producción Pecuaria'),
        (SPA, 'Sistemas de Producción Agrícola'),
        (AGRO, 'Agropecuario'),
        (DS, 'Desarrollo Sustentable'),
    ]

    desc = models.CharField(
        max_length=1,
        choices=GRUPOS,
        default='A')

    carrera = models.CharField(
        max_length=55,
        choices=CARRERAS,
        default=GENE)

    def __str__(self):
        if self.carrera == 'General':
            return (f'"{self.desc}"')
        else:
            return (f'{self.carrera} - "{self.desc}"')


class Alumno(models.Model):
    """
    Alumno model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grupo = models.ForeignKey(
        Grupo, 
        on_delete=models.CASCADE)

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