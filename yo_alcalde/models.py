from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vecino(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=100)
    amaterno = models.CharField(max_length=100)
    nacimiento = models.DateField()
    genero = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apaterno} {self.amaterno}"
