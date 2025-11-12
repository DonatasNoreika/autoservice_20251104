from django.shortcuts import render
from .models import Car, Service, Order

def index(request):
    context = {
        "num_cars": Car.objects.count(),
        "num_services": Service.objects.count(),
        "num_orders_completed": Order.objects.filter(status='o').count(),
    }
    return render(request, template_name="index.html", context=context)


def cars(request):
    context = {
        "cars": Car.objects.all(),
    }
    return render(request, template_name="cars.html", context=context)

def car(request, pk):
    context = {
        "car": Car.objects.get(pk=pk)
    }
    return render(request, template_name="car.html", context=context)