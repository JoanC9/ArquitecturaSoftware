from django.db import models

# Create your models here.

class Persona (models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    celular = models.BigIntegerField()
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}. Vive en {self.ciudad}. Numero {self.celular}'
    
class Articulo (models.Model):
    
    nombre = models.CharField(max_length=30)
    color = models.CharField(max_length=30, blank=True, null=True)
    codigo = models.IntegerField()
    
    def __str__(self) -> str:
        return f'Articulo {self.nombre}. Color {self.color}. Codigo{self.codigo}'
    
    
class Enviado (models.Model):
    
    sucursal = models.CharField(max_length=30)
    fecha = models.DateField(verbose_name='Fecha de Envio')
    enviado = models.BooleanField(verbose_name='Entregado')
    
    def __str__(self) -> str:
        return f'Enviado a sucursal {self.sucursal}. El día {self.fecha}. Entregado{self.enviado}'