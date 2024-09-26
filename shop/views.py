from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def shop(request):
    artikels = Artikel.objects.all
    ctx = {'artikels':artikels}
    return render(request, 'shop/shop.html', ctx)

def card(request):
    return render(request, 'shop/card.html')

def checkout(request):
    return render(request, 'shop/checkout.html')