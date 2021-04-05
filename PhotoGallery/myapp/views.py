from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request):
    return HttpResponse("hi")

def index(request):
    return render(request,"index.html")

