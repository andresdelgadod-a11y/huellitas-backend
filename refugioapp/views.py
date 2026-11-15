from rest_framework import viewsets
from .models import Refugio, Mascota
from .serializers import RefugioSerializer, MascotaSerializer

class RefugioViewSet(viewsets.ModelViewSet):
    queryset = Refugio.objects.all()
    serializer_class = RefugioSerializer


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
