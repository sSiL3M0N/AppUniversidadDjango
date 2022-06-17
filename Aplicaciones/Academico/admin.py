from django.contrib import admin

# Register your models here.
from .models import Curso,Docente


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'datos', 'colorearCreditos')
    ordering = ('id',)

    #list_filter = ('creditos')
    #search_fields = ('nombre','creditos')
    list_display_links = ('datos',)

    fieldsets = (
        ("Normal", {
            'fields':('nombre','docente')
        })
        ,
        ('Avanzado', {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('creditos',)
        })
    )

    def datos(self, obj):
        return obj.nombre.upper()

    datos.short_description = "Curso Mayus"
    datos.empty_value_display = "???"
    datos.admin_order_field= 'nombre'

#admin.site.register(Curso)
admin.site.register(Docente)