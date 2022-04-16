from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bike, Socket
from .forms import MaintenanceForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bikes_index(request):
    bikes = Bike.objects.all()
    return render(request, 'bikes/index.html', {'bikes': bikes})

def bikes_detail(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
    id_list = bike.tools.all().values_list('id')
    sockets_bike_doesnt_have = Socket.objects.exclude(id__in=id_list)
    maintenance_form = MaintenanceForm()
    return render(request, 'bikes/detail.html', { 'bike': bike, 'maintenance_form': maintenance_form, 'sockets': sockets_bike_doesnt_have})

def add_maintenance(request, bike_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_change = form.save(commit=False)
        new_change.bike_id = bike_id
        new_change.save()
    return redirect('detail', bike_id=bike_id)

def assoc_tool(request, bike_id, socket_id):
    Bike.objects.get(id=bike_id).tools.add(socket_id)
    return redirect('detail', bike_id=bike_id)

class BikeCreate(CreateView):
    model=Bike
    fields = ['model', 'brand', 'hours', 'vin', 'headNo', 'caseNo', 'owner']

class BikeUpdate(UpdateView):
    model=Bike
    fields = '__all__'

class BikeDelete(DeleteView):
    model=Bike
    success_url = '/bikes'

class Socketlist(ListView):
    model = Socket

class SocketCreate(CreateView):
    model = Socket
    fields = '__all__'
