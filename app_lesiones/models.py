from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    deporte = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.deporte})"


class Lesion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"{self.tipo} - {self.estudiante.nombre}"


class Tratamiento(models.Model):
    lesion = models.ForeignKey(Lesion, on_delete=models.CASCADE)
    descripcion = models.TextField()
    duracion_dias = models.IntegerField()

    def __str__(self):
        return f"Tratamiento para {self.lesion.tipo}"
