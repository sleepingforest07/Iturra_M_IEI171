from django.db import models

# Create your models here.

class Socios_Del_Club(models.Model):
    Nombre_Socio = models.CharField(max_length=50, verbose_name="Nombre_Socio")
    Fecha_Incorporacion = models.DateField(verbose_name="Fecha_Incorporacion")
    Fecha_nacimiento = models.DateField(verbose_name="Año_nacimiento")
    Telefono = models.CharField(max_length=30, verbose_name="Telefono")
    Correo_Electronico = models.EmailField(verbose_name="Correo_Electronico")
    Sexo = models.CharField(max_length=50, verbose_name="Sexo")
    estado= models.CharField(max_length=50, verbose_name="estado")
    observacion = models.CharField(max_length=200, verbose_name="observacion")
    

def __str__(self):
    fila = "Nombre: " + self.Nombre_Socio + "Fecha de incorporacion: " + self.Fecha_Incorporacion + "Fecha nacimiento" + self.Fecha_nacimiento + "Telefono" + self.Telefono + "Correo Electronico" + self.Correo_Electronico + "Sexo" + self.Sexo + "estado" + self.estado + "observacion" + self.observacion
    return fila

