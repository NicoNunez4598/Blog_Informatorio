from django.db import models

# Create your models here.

class Categoria(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Categoria Activa / Categoria Desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        
        return self.nombre

class Autor(models.Model):

    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres del Autor', max_length=255, null=False, blank=False)
    apellidos = models.CharField('Apellidos del Autor', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    correo = models.EmailField('Correo Electronico', null=False, blank=False)
    estado = models.BooleanField('Autor Activo / Autor No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        
        return "{0},{1}".format(self.apellidos, self.nombres)