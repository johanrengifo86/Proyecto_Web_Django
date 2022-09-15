from email.mime import image
from msilib import MSIMODIFY_DELETE
from tabnanny import verbose
from turtle import update
from venv import create
from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # Clase que da nombre al las tablas correspondientes en la base de datos
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo


