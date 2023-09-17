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
