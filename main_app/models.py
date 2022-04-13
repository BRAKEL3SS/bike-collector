from django.db import models
from django.urls import reverse

# Create your models here.
class Socket(models.Model):
    size = models.IntegerField()
    drive = models.CharField(max_length=10)

    def __str__(self):
        return self.size
    
    def get_absolute_url(self):
        return reverse('sockets_detail', kwargs={'pk': self.id})


class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=6, decimal_places=2)
    tools = models.ManyToManyField(Socket)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bike_id': self.id})


class OilChange(models.Model):
    date = models.DateField()
    filterChange = models.BooleanField('Oil Filter Change', default=False)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.filterChange} filter on {self.date}"

    class Meta:
        ordering = ['-date']