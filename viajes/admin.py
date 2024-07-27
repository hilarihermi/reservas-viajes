from django.contrib import admin
from .models import Destino, Viaje, Cliente, Reserva

admin.site.register(Destino)
admin.site.register(Viaje)
admin.site.register(Cliente)
admin.site.register(Reserva)