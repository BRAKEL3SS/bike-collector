from django.db import models

# Create your models here.
class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.model
