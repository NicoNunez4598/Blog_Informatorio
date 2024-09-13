from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def generales(request):
    return render(request, 'generales.html')
