from django.shortcuts import render
from.models import *
from django.http import HttpRequest


def main(request):
    template = 'main/main.html'
    products = Product.objects.all()
    collections = Collection.objects.all()
    types = ProductType.objects.all()
    sizes = ProductSize.objects.all()

    context = {
        'products': products,
        'collections': collections,
        'types': types,
        'sizes': sizes
    }
    return render(request, template, context)