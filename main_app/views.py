from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bike, Socket
from .forms import OilChangeForm

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
    oilchange_form = OilChangeForm()
    return render(request, 'bikes/detail.html', { 'bike': bike, 'oilchange_form': oilchange_form})

def add_oilchange(request, bike_id):
    form = OilChangeForm(request.POST)
    if form.is_valid():
        new_change = form.save(commit=False)
        new_change.bike_id = bike_id
        new_change.save()
    return redirect('detail', bike_id=bike_id)

class BikeCreate(CreateView):
    model=Bike
    fields = '__all__'

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
