# Django
from django.db import models


class Materia(models.Model):
    clave_materia = models.CharField(max_length=10)
    nombre_materia = models.CharField(max_length=55)

    def __str__(self):
        return self.nombre_materia


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
        default=('A','A'))

    carrera = models.CharField(
        max_length=55,
        choices=CARRERAS,
        default=CARRERAS[0])

    def __str__(self):
        if self.carrera == 'General':
            return (f'"{self.desc}"')
        else:
            return (f'{self.carrera} - "{self.desc}"')


class Semestre(models.Model):
    SEMESTRES = [
        ('1', 'PRIMERO'),
        ('2', 'SEGUNDO'),
        ('3', 'TERCERO'),
        ('4', 'CUARTO'),
        ('5', 'QUINTO'),
        ('6', 'SEXTO'),
    ]

    descripcion = models.CharField(
        max_length=1,
        choices=SEMESTRES,
        default=('1','PRIMERO'))

    fecha_inicio = models.DateField("Fecha de inicio")
    fecha_fin = models.DateField("Fecha fin")
    
    def __str__(self):
        return (f'{self.descripcion}° Semestre - {self.fecha_inicio.month}/{self.fecha_inicio.year} - {self.fecha_fin.month}/{self.fecha_fin.year}')