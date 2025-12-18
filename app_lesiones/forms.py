from django import forms
from django.core.exceptions import ValidationError
from .models import Estudiante, Lesion, Tratamiento


# =====================
#  FORMULARIO ESTUDIANTE
# =====================
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

    # Validación nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if len(nombre) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    # Validación edad
    def clean_edad(self):
        edad = self.cleaned_data.get("edad")
        if edad <= 0:
            raise ValidationError("La edad debe ser mayor que 0.")
        return edad

    # Validación deporte
    def clean_deporte(self):
        deporte = self.cleaned_data.get("deporte")
        if not deporte.strip():
            raise ValidationError("El deporte no puede estar vacío.")
        return deporte


# =====================
#  FORMULARIO LESIÓN
# =====================
class LesionForm(forms.ModelForm):
    class Meta:
        model = Lesion
        fields = '__all__'

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        if len(descripcion.strip()) < 10:
            raise ValidationError("La descripción debe tener al menos 10 caracteres.")
        return descripcion


# =====================
#  FORMULARIO TRATAMIENTO
# =====================
class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        if len(descripcion.strip()) < 5:
            raise ValidationError("La descripción del tratamiento debe tener al menos 5 caracteres.")
        return descripcion

    def clean_duracion_dias(self):
        duracion = self.cleaned_data.get("duracion_dias")
        if duracion <= 0:
            raise ValidationError("La duración debe ser mayor que 0.")
        return duracion
