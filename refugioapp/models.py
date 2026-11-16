from django.db import models


class Refugio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    ESTADOS = [
        ('adopcion', 'En adopción'),
        ('perdida', 'Perdida'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    edad = models.IntegerField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='adopcion')
    ultima_ubicacion = models.CharField(max_length=200, blank=True)
    contacto = models.CharField(max_length=20, blank=True)
    refugio = models.ForeignKey(
        Refugio,
        on_delete=models.CASCADE,
        related_name="mascotas",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.nombre} - {self.tipo} ({self.get_estado_display()})"