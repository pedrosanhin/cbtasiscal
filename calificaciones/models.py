# Django
from django.db import models

from usuarios.models import Alumno, Maestro


class Materia(models.Model):
    clave_materia = models.CharField(max_length=10)
    nombre_materia = models.CharField(max_length=55)

    def __str__(self):
        return self.nombre_materia


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


class Calificaciones(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    cal_primer_parcial = models.IntegerField(blank=True, null=True)
    cal_segundo_parcial = models.IntegerField(blank=True, null=True)
    cal_tercer_parcial = models.IntegerField(blank=True, null=True)

    def get_promedio(self):
        return (self.cal_primer_parcial+self.cal_segundo_parcial+self.cal_tercer_parcial)/3

    def __str__(self):
        return (f'Calificaciones del alumno {self.alumno} en la materia {self.materia}')