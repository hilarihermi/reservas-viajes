from django.db import models
from django.core.exceptions import ValidationError

def validate_telefono(value):
    if not value.isdigit() or len(value) < 8:
        raise ValidationError('El teléfono debe tener al menos 8 dígitos.')

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Viaje(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    fecha_salida = models.DateField()
    fecha_regreso = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.fecha_salida >= self.fecha_regreso:
            raise ValidationError('La fecha de salida debe ser anterior a la fecha de regreso.')

    def __str__(self):
        return f"Viaje a {self.destino.nombre} desde {self.fecha_salida} hasta {self.fecha_regreso}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, validators=[validate_telefono])

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} para el viaje a {self.viaje.destino.nombre}"
