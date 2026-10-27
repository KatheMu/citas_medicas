from django.db import models

class CitaMedica(models.Model):
    paciente = models.CharField(max_length=100)
    rut = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField() 

    def __str__(self):
        return f"Cita de {self.paciente} - {self.especialidad} ({self.fecha_hora})"
