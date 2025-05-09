from django.contrib import admin
from .models import Vacante # Importa tu modelo

# Registra tu modelo para que aparezca en el admin
@admin.register(Vacante)
class VacanteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'ubicacion', 'fecha_publicacion', 'activo') # Columnas a mostrar en la lista
    list_filter = ('activo', 'fecha_publicacion', 'empresa') # Filtros laterales
    search_fields = ('titulo', 'descripcion', 'empresa') # Campos por los que buscar
    list_editable = ('activo',) # Permite editar 'activo' directamente en la lista
    date_hierarchy = 'fecha_publicacion' # Navegación por fechas