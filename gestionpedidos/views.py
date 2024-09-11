from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import Articulo
# Create your views here.

def buscar (request):
    
    return render(request,'buscar.html')

def encontrar (request):
    
    if request.GET['art']:
        
        articulo_buscado = request.GET['art']
        
        buscar_art_bd = Articulo.objects.filter(nombre__icontains=articulo_buscado)
        
        if buscar_art_bd:
            
            cntx = {
                
                'introducido' : articulo_buscado,
                'encontrado' : buscar_art_bd
            }
            
            return render(request,'encontrar.html', cntx)
        
        else:
            
            mensaje = 'El articulo buscado no se encuentra'
    else:
        
        mensaje = 'El campo se dejo en blanco'
        
    return HttpResponse(mensaje)
        