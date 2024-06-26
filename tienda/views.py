from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {}
    return render(request, 'tienda/index.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'mensaje': 'Enviado correctamente', 'form': ContactForm()}
        else:
            context = {'form': form}
    else:
        context = {'form': ContactForm()}

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
