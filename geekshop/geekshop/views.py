from django.shortcuts import render
from mainapp.models import Product

def index(request):
    title = 'магазин'
    products = Product.objects.all()[:2]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html')

def contacts(request):
    return render(request, 'geekshop/contact.html')