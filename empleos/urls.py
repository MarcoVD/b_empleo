from django.urls import path
from .views import VacanteListView, VacanteDetailView, index # Importa tus vistas

app_name = 'empleos' # Define un namespace para las URLs de esta app

urlpatterns = [
    path('', VacanteListView.as_view(), name='lista_vacantes'), # Página principal de empleos (lista)
    path('vacante/<int:pk>/', VacanteDetailView.as_view(), name='detalle_vacante'), # Detalle de vacante por ID (pk)
    # path('inicio/', index, name='inicio'), # Si creaste la vista index
]