from django.contrib import admin
from .models import Productos, Contacto, TipoProducto

# Register your models here.

admin.site.register(Productos)
admin.site.register(Contacto)
admin.site.register(TipoProducto)