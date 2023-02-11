from django.db import models

# Create your models here.
class Owner(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)