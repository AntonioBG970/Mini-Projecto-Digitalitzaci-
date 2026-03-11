from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Producto
# Create your views here.
def inicio(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'core/inicio.html', {
        'productos': productos,
        'categorias': categorias
    })

def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'core/producto_detalle.html', {'producto': producto})