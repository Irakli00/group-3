from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView

from .models import Car
from .forms import CarForm

def car_landing_page(request):
    return render(request,'car/car_landing.html')

class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car_detail.html'

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car/car_edit.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car/car_edit.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car/car_delete.html'
    success_url = reverse_lazy('car_list')
