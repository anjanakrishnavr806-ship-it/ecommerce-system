from django.shortcuts import render
from .models import Product

def store(request):
    products = Product.objects.filter(available=True)
    context = {'products': products}
    return render(request, 'store.html', context)
