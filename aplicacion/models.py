from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Consola(models.Model):
    nombre = models.CharField(max_length=30)
    empresa = models.CharField(max_length=40)
    cantidad = models.IntegerField()

    class Meta:
        ordering = ["nombre"]

    def __str__ (self):
        return f"{self.nombre}"
    
class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    
    def __str__ (self):
        return f"{self.nombre}"

class Todos_los_productos(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    cantidad = models.IntegerField()

class Quienes_somos(models.Model):
    todo = models.CharField(max_length=10000)

class Argames(models.Model):
    todo = models.CharField(max_length=10000)