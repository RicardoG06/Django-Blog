from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria', max_length = 100 , null = False , blank = False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False , auto_now_add = True) #auto_now_add = True -> La fecha de creacion no se modifica.

    class Meta:
        verbose_name = 'Categoria' #Manera por la cual se identifica cada vez que se mencione de manera individial en el sitio de administracion de django
        verbose_name_plural = 'Categorias'
    def __str__(self):
        return self.nombre #Me retorna por default el nombre para verlo en el administrador de django

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField('Nombres de Autor', max_length = 255 , null = False , blank = False)
    apellidos = models.CharField('Apellidos de autor' , max_length = 255 , null = False , blank = False)
    facebook = models.URLField('Facebook', null = True , blank = True) #blank = True -> Se puede dejar en blanco
    twitter = models.URLField('Twitter', null = True , blank = True)
    instagram = models.URLField('Instagram', null = True , blank = True)
    web = models.URLField('Web', null = True , blank = True)
    correo = models.EmailField('Correo Electronico' , blank = False , null = False) #blank = False -> No se puede dejar en blanco
    estado = models.BooleanField('Autor Activo/ No activo' , default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False , auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos , self.nombres)
