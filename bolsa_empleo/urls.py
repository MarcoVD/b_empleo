"""
URL configuration for bolsa_empleo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Asegúrate de importar include
from empleos.views import  VacanteListView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluye las URLs de la app 'empleos' bajo el prefijo 'ofertas/' (o el que prefieras)
    path('ofertas/', include('empleos.urls', namespace='empleos')),

# URLs de autenticación de Django (login, logout, cambio de contraseña, etc.)
    # Usará las plantillas que creemos en 'templates/registration/'
    path('cuentas/', include('django.contrib.auth.urls')),

    # Nueva ruta para nuestra interfaz de administración personalizada
    path('administracion/', include('empleos.admin_urls', namespace='admin_empleos')), # Usaremos un archivo separado para estas URLs
    path('', VacanteListView.as_view(), name='home'),
    # Si quieres que la raíz del sitio muestre las ofertas directamente:
    #path('', include('empleos.urls', namespace='empleos')),
    # Si creaste una vista 'index' en empleos y quieres que sea la raíz:
    # path('', include('empleos.urls', namespace='empleos')), # Asegúrate que la raíz esté definida en empleos/urls.py
]