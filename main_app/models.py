from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Socket(models.Model):
    size = models.IntegerField()
    drive = models.CharField(max_length=10)

    def __str__(self):
        return self.size
    
    def get_absolute_url(self):
        return reverse('sockets_index')


class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=6, decimal_places=2)
    vin = models.CharField(max_length=30)
    headNo = models.CharField(max_length=30)
    caseNo = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    tools = models.ManyToManyField(Socket)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bike_id': self.id})


class Maintenance(models.Model):
    date = models.DateField()
    maintenance = models.TextField(max_length=300)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.maintenance}"

    class Meta:
        ordering = ['-date']