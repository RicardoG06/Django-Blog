from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor


class CategoriaAdmin(admin.ModelAdmin): #Creando entorno de trabajo para administracion de django
    search_fields = ['nombre'] #Buscar por: nombre , indiferente a mayusculas o minusculas
    list_display = ('nombre','estado','fecha_creacion',)#atributos que queremos mostrar en admin. de django
    resource_class = CategoriaResource

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres' , 'apellidos' , 'correo']
    list_display = ('nombres','apellidos','correo','estado','fecha_creacion',)


# Register your models here.
admin.site.register(Categoria,CategoriaAdmin) #Recibe 2 parametros , 1 el nombre del modelo y el otro la clase Admin para que se vea mejor la admin. de django
admin.site.register(Autor , AutorAdmin)
admin.site.register(Post)
