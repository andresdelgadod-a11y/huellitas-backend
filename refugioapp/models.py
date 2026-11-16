from django.db import models


class Refugio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    edad = models.IntegerField()
    descripcion = models.TextField()
    refugio = models.ForeignKey(Refugio, on_delete=models.CASCADE, related_name="mascotas")

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"