from django.shortcuts import render
from .models import SnacksCategory, SnackItem

def index(request):
    categories = SnacksCategory.objects.all()
    return render(request, 'index.html', {'categories':categories})

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    categories = SnacksCategory.objects.all()
    snackitems = SnackItem.objects.all()
    return render(request, 'shop.html', {'categories':categories, 'snackitems':snackitems})

def about(request):
    return render(request, 'about.html')

def export(request):
    return render(request, 'export.html')


def product(request, snack_name):
    snack = SnackItem.objects.get(name=snack_name)
    return render(request, 'product.html', {'snack':snack})

def analyse(request):
    return render(request, 'analyse.html')