from django.shortcuts import render
from . import models

def home(request):
    products = models.Product.objects.all().filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'home.html', context)
