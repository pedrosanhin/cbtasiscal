"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    """
    Usuario model.

    Proxy model that extends the base data of User with other information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username


class Maestro(Usuario):
    """
    Maestro model.
    """
    
    nombres = models.TextField(max_length=80)
    apellido_paterno = models.TextField(max_length=50)
    apellido_materno = models.TextField(max_length=50, blank=True)

    def __str__(self):
        """Return name."""
        return "{} {} {}".format(self.nombres, self.apellido_paterno, self.apellido_materno)
    

class Alumno(Usuario):
    """
    Alumno model.
    """
    
    no_control = models.TextField(max_length=24, blank=True)

    nombres = models.TextField(max_length=80)
    apellido_paterno = models.TextField(max_length=50)
    apellido_materno = models.TextField(max_length=50, blank=True)
    
    def __str__(self):
        """Return name."""
        if self.apellido_materno:
            return "{} {} {}".format(self.nombres, self.apellido_paterno, self.apellido_materno)
        else:
            return "{} {}".format(self.nombres, self.apellido_paterno)