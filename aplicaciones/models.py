from django.db import models

class Aplicaciones(models.Model):
    nombre = models.CharField(max_length=100)