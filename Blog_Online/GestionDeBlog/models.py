from django.db import models

# Create your models here.

class Categoria(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Categoria Activa / Categoria Desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'
    
    def __str__(self):
        
        return self.nombre

class Autor(models.Model):

    