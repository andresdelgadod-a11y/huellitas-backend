from rest_framework import viewsets
from .models import Refugio, Mascota
from .serializers import RefugioSerializer, MascotaSerializer


class RefugioViewSet(viewsets.ModelViewSet):
    queryset = Refugio.objects.all()
    serializer_class = RefugioSerializer


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        estado = self.request.query_params.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)
        return queryset
