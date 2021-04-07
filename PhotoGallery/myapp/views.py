from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def test(request):
    items = Item.objects.all()
    context = {
        "items" : items,
    }
    return render(request,"test.html",context)
    

def index(request):
    items = Item.objects.all()
    context = {
        "items" : items,
    }
    return render(request,"index.html",context)

