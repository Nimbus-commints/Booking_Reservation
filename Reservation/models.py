from django.db import models

# Create your models here.


class Booking(models.Model):
    nombre = models.CharField(max_length=255)
    dia_de_reserva = models.DateField()
    n_personas = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.first_name
