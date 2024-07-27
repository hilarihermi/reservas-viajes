#from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Destino, Viaje, Cliente, Reserva
from .serializers import DestinoSerializer, ViajeSerializer, ClienteSerializer, ReservaSerializer

class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

@api_view(['GET'])
def custom_api(request):
    data = {'message': 'Esta es una API personalizada'}
    return Response(data)