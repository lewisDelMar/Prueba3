from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'tienda/index.html', context)

def contacto(request):
    context = {}
    return render(request, 'tienda/contacto.html', context)

def accesorios(request):
    context = {}
    return render(request, 'tienda/accesorios.html', context)

def carrito(request):
    context = {}
    return render(request, 'tienda/carrito.html', context)

def macetas(request):
    context = {}
    return render(request, 'tienda/macetas.html', context)

def plantas(request):
    context = {}
    return render(request, 'tienda/plantas.html', context)