from django.db import models

# Create your models here.


class Booking(models.Model):
    nombre = models.CharField(max_length=255)
    dia_de_reserva = models.DateField()
    n_de_personas = models.SmallIntegerField(default=10)
    hora_de_reserva = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.title
