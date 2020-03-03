from django.shortcuts import render
from.models import *
from django.http import HttpRequest


def main(request):
    template = 'main/main.html'
    products = Product.objects.all()
    collections = Collection.objects.all()
    types = ProductType.objects.all()
    sizes = ProductSize.objects.all()
    genders = HumanGender.objects.all()

    context = {
        'products': products,
        'collections': collections,
        'types': types,
        'sizes': sizes,
        'genders': genders
        }
    return render(request, template, context)


def current_gender(request, slug):
    template = 'main/main.html'

    products = Product.objects.filter(gender__slug=slug)
    collections = Collection.objects.all()
    types = ProductType.objects.all()
    sizes = ProductSize.objects.all()
    genders = HumanGender.objects.all()

    context = {
        'products': products,
        'collections': collections,
        'types': types,
        'sizes': sizes,
        'genders': genders
        }
    return render(request, template, context)