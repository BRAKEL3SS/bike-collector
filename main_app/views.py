from django.shortcuts import render
from django.http import HttpResponse
from .models import Bike

# Create your views here.

def home(request):
    return HttpResponse('<h1>hello</h1>')

def about(request):
    return render(request, 'about.html')

def bikes_index(request):
    bikes = Bike.objects.all()
    return render(request, 'bikes/index.html', {'bikes': bikes})

def bikes_detail(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
    return render(request, 'bikes/detail.html', { 'bike': bike})