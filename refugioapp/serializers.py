from rest_framework import serializers
from .models import Refugio, Mascota


class RefugioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refugio
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):
    nombre_refugio = serializers.CharField(source='refugio.nombre', read_only=True, allow_null=True)

    class Meta:
        model = Mascota
        fields = [
            'id', 'nombre', 'tipo', 'edad', 'descripcion',
            'estado', 'ultima_ubicacion', 'contacto',
            'refugio', 'nombre_refugio',
        ]