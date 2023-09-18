from rest_framework import serializers
from .models import Clientes

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
        # Doble comillas me trae todos los campos del modelo.
        