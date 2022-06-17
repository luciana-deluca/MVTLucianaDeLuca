from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=20)
    fechadenac = models.DateField()
    edad = models.IntegerField()
