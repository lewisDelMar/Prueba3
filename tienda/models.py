from django.db import models

# Create your models here.

class Productos(models.Model):
    id_produ        = models.AutoField(db_column = 'idProdu', primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    precio          = models.IntegerField()
    foto            = models.ImageField(upload_to='media', null=True)


class Contacto(models.Model):
    id_contacto     = models.AutoField(db_column = 'idContacto', primary_key=True)
    nombrepri       = models.CharField(max_length=50)
    apellidopa      = models.CharField(max_length=50)
    telefono        = models.IntegerField()
    email           = models.EmailField()
    mensaje         = models.TextField()