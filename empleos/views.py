# empleos/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # Importa los mixins
from .models import Vacante
from .forms import VacanteForm  # Importa el formulario


# --- Vistas Públicas (las que ya tenías) ---
class VacanteListView(ListView):
    model = Vacante
    template_name = 'empleos/vacante_list.html'
    context_object_name = 'vacantes'
    queryset = Vacante.objects.filter(activo=True).order_by('-fecha_publicacion')
    paginate_by = 10


class VacanteDetailView(DetailView):
    model = Vacante
    template_name = 'empleos/vacante_detail.html'
    context_object_name = 'vacante'
    queryset = Vacante.objects.filter(activo=True)


def index(request):
    ultimas_vacantes = Vacante.objects.filter(activo=True).order_by('-fecha_publicacion')[:5]
    context = {
        'ultimas_vacantes': ultimas_vacantes
    }
    return render(request, 'empleos/index.html', context)


# --- Mixin para verificar si es Staff (Opcional pero recomendado) ---
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Verifica que el usuario esté logueado Y sea miembro del staff.
    """

    def test_func(self):
        # user.is_staff es un booleano en el modelo User de Django
        # Asegúrate que los usuarios administradores tengan esta casilla marcada en el admin de Django
        return self.request.user.is_staff

    def handle_no_permission(self):
        # Si no es staff, lo redirige al login
        return super().handle_no_permission()


# --- Vistas de Administración ---

# Vista para el Dashboard/Lista de Admin (Usa StaffRequiredMixin)
class AdminVacanteListView(StaffRequiredMixin, ListView):
    model = Vacante
    template_name = 'empleos/admin/dashboard.html'  # Nueva plantilla para el dashboard
    context_object_name = 'vacantes'
    paginate_by = 15  # Puedes tener diferente paginación aquí
    # Muestra todas las vacantes (activas e inactivas) ordenadas por fecha
    queryset = Vacante.objects.all().order_by('-fecha_publicacion')
    login_url = reverse_lazy('login')  # Redirige aquí si no está logueado o no es staff


# Vista para Crear Vacante (Usa StaffRequiredMixin)
class AdminVacanteCreateView(StaffRequiredMixin, CreateView):
    model = Vacante
    form_class = VacanteForm  # Usa nuestro formulario personalizado
    template_name = 'empleos/admin/vacante_form.html'  # Plantilla para el formulario
    # Redirige al dashboard después de crear exitosamente
    success_url = reverse_lazy('admin_empleos:admin_dashboard')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        # Añade contexto extra a la plantilla si es necesario
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Crear Nueva Vacante'
        context['nombre_boton'] = 'Crear Vacante'
        return context

    # (Opcional) Puedes añadir lógica extra cuando el formulario es válido
    def form_valid(self, form):
        form.instance.creado_por = self.request.user # Ejemplo: asignar usuario creador
        return super().form_valid(form)


# Vista para Editar Vacante (Usa StaffRequiredMixin)
class AdminVacanteUpdateView(StaffRequiredMixin, UpdateView):
    model = Vacante
    form_class = VacanteForm
    template_name = 'empleos/admin/vacante_form.html'  # Reutiliza la plantilla del formulario
    success_url = reverse_lazy('admin_empleos:admin_dashboard')
    context_object_name = 'vacante'  # Nombre del objeto en la plantilla
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = f'Editar Vacante: {self.object.titulo}'
        context['nombre_boton'] = 'Guardar Cambios'
        return context


# Vista para Eliminar Vacante (Usa StaffRequiredMixin)
class AdminVacanteDeleteView(StaffRequiredMixin, DeleteView):
    model = Vacante
    template_name = 'empleos/admin/vacante_confirm_delete.html'  # Plantilla de confirmación
    success_url = reverse_lazy('admin_empleos:admin_dashboard')
    context_object_name = 'vacante'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = f'Confirmar Eliminación: {self.object.titulo}'
        return context
