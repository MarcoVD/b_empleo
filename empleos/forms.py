# empleos/forms.py
from django import forms
from .models import Vacante


class VacanteForm(forms.ModelForm):
    """
    Formulario basado en el modelo Vacante para crear y editar.
    """

    class Meta:
        model = Vacante
        # Incluye todos los campos que quieres que sean editables en el formulario
        fields = [
            'titulo',
            'descripcion',
            'empresa',
            'ubicacion',
            'salario',
            # 'tipo_contrato', # Descomenta si añadiste este campo
            'activo',  # Permite marcar/desmarcar si la vacante está activa
        ]
        # (Opcional) Personaliza los widgets si quieres usar diferentes controles HTML
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 5}),  # Hace el campo de descripción más grande
            'salario': forms.NumberInput(attrs={'step': '0.01'}),  # Ayuda con la entrada de decimales
        }
        # (Opcional) Personaliza las etiquetas si quieres que sean diferentes al verbose_name del modelo
        labels = {
            'titulo': 'Título Principal de la Oferta',
            'activo': '¿Publicar esta vacante?'
        }
        # (Opcional) Añade textos de ayuda
        help_texts = {
            'salario': 'Dejar en blanco si es confidencial.',
        }

    # (Opcional) Puedes añadir validaciones personalizadas aquí si es necesario
    # def clean_titulo(self):
    #     titulo = self.cleaned_data.get('titulo')
    #     if len(titulo) < 10:
    #         raise forms.ValidationError("El título debe tener al menos 10 caracteres.")
    #     return titulo
