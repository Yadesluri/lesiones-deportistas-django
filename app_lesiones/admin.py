from django.contrib import admin
from .models import Estudiante, Lesion, Tratamiento

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'deporte')
    search_fields = ('nombre', 'deporte')

@admin.register(Lesion)
class LesionAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'fecha', 'estudiante')
    list_filter = ('fecha', 'estudiante')  # ✅ Campos REALES: fecha y estudiante
    search_fields = ('tipo', 'descripcion')  # ✅ descripcion existe

@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('lesion', 'descripcion', 'duracion_dias')  # ✅ descripcion en lugar de tipo_tratamiento
    list_filter = ('duracion_dias',)  # ✅ Filtra por duración o por lesion
    search_fields = ('descripcion',)