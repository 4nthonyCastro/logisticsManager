from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.views import generic
from django.utils import timezone
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request): 
    return render(request, 'pages/about.html')

def products(request):
    return render(request, 'pages/products.html')
