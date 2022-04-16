from django.contrib import admin
from .models import Bike, Maintenance

# Register your models here.
admin.site.register(Bike)
admin.site.register(Maintenance)