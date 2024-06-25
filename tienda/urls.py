from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('accesorios/', views.accesorios, name='accesorios'),
    path('carrito/', views.carrito, name='carrito'),
    path('macetas/', views.macetas, name='macetas'),
    path('plantas/', views.plantas, name='plantas'),
]