from django.db import models
from django.urls import reverse

# Create your models here.
class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bike_id': self.id})


class OilChange(models.Model):
    date = models.DateField()
    filter = models.BooleanField(default=False)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.filter} filter on {self.date}"