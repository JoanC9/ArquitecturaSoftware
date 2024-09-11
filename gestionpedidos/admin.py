from django.contrib import admin
from gestionpedidos.models import Persona,Articulo,Enviado
# Register your models here.

class AdminPersona (admin.ModelAdmin):
    
    list_display = ('nombre', 'apellido', 'celular',)
    search_fields = ('nombre','apellido',)
    list_filter = ('celular',)
    
class AdminArticulo (admin.ModelAdmin):
    
    list_display = ('nombre','codigo',)
    search_fields = ('nombre',)
    list_filter = ('codigo',)
    
class AdminEnviado (admin.ModelAdmin):
    
    list_display = ('sucursal','fecha','enviado',)
    search_fields = ('sucursal',)
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'
    
admin.site.register(Persona,AdminPersona)
admin.site.register(Articulo,AdminArticulo)
admin.site.register(Enviado,AdminEnviado)

