from .models import Clientes
from rest_framework import viewsets
from .serializer import ClientesSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset= Clientes.objects.all()
    serializer_class= ClientesSerializer

