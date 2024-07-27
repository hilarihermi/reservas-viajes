
from rest_framework import serializers
from .models import Destino, Viaje, Cliente, Reserva

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'