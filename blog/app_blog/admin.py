from django.contrib import admin

# Register your models here.

from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(admin.ModelAdmin):
    class Meta:
        model = Categoria

class CategoriaResource(admin.ModelAdmin):
    class Meta:
        model = Autor

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):#Barra de busqueda y impot/export
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)
    resource = CategoriaResource

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin): 
    search_fields  = ['nombres','apellidos', 'correo']
    list_display = ('nombres','apellidos','correo','estado','fecha_creacion',)
    resource = CategoriaResource

    
class ProdcutAdminManager(admin.ModelAdmin):  
    exclude = ('slug',)                         

admin.site.register(Post, ProdcutAdminManager)  
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)



