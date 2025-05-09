from django.db import models
from django.utils import timezone # Para la fecha de publicación

class Vacante(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título de la Vacante")
    descripcion = models.TextField(verbose_name="Descripción del Puesto")
    empresa = models.CharField(max_length=150, verbose_name="Nombre de la Empresa")
    ubicacion = models.CharField(max_length=100, verbose_name="Ubicación")
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Salario (Opcional)")
    # Puedes añadir más campos como: tipo_contrato, categoria, requisitos, etc.
    # Por ejemplo:
    # TIPO_CONTRATO_CHOICES = [
    #     ('TIEMPO_COMPLETO', 'Tiempo Completo'),
    #     ('MEDIO_TIEMPO', 'Medio Tiempo'),
    #     ('PROYECTO', 'Por Proyecto'),
    # ]
    # tipo_contrato = models.CharField(max_length=20, choices=TIPO_CONTRATO_CHOICES, default='TIEMPO_COMPLETO')
    fecha_publicacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Publicación")
    activo = models.BooleanField(default=True, verbose_name="¿Está Activa?")

    def __str__(self):
        return f"{self.titulo} en {self.empresa}"

    class Meta:
        verbose_name = "Vacante"
        verbose_name_plural = "Vacantes"
        ordering = ['-fecha_publicacion'] # Ordenar por fecha más reciente primero
