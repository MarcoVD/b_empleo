# empleos/admin_urls.py
from django.urls import path
from .views import (
    AdminVacanteListView,
    AdminVacanteCreateView,
    AdminVacanteUpdateView,
    AdminVacanteDeleteView,
)

app_name = 'admin_empleos'  # Namespace definido en bolsa_empleo/urls.py

urlpatterns = [
    # Ruta principal del dashboard de administración (lista de vacantes)
    path('', AdminVacanteListView.as_view(), name='admin_dashboard'),

    # Ruta para crear una nueva vacante
    path('vacantes/nueva/', AdminVacanteCreateView.as_view(), name='admin_vacante_crear'),

    # Ruta para editar una vacante existente (usa el 'pk' de la vacante)
    path('vacantes/editar/<int:pk>/', AdminVacanteUpdateView.as_view(), name='admin_vacante_editar'),

    # Ruta para eliminar una vacante existente (usa el 'pk')
    path('vacantes/eliminar/<int:pk>/', AdminVacanteDeleteView.as_view(), name='admin_vacante_eliminar'),

    # Puedes añadir más URLs aquí para otras funcionalidades (ej. ver aplicaciones)
    # path('aplicaciones/', alguna_vista_aplicaciones, name='admin_aplicaciones'),
]
