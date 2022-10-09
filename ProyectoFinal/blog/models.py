from tabnanny import verbose
from urllib import request
from django.db import models

class Reserva (models.Model):

    class Meta:
        verbose_name_plural = "Reservas"

    nombre = models.CharField(max_length = 30)
    fecha = models.DateField()
    comensales = models.IntegerField()

    def __str__(self):
        return self.nombre


class Cliente (models.Model):

    class Meta:
        verbose_name_plural = "Clientes"

    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 30)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
  

class Bar (models.Model):

    class Meta:
        verbose_name_plural = "Bares"

    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 30)
    especialidad = models.CharField(max_length = 300)

    def __str__(self):
        return self.nombre
