from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.views import generic
from django.utils import timezone
from django.urls import reverse
from django.template import loader

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'latest_question_list' 
    def get_queryset(self): 
        return Question.objects.order_by('-pub_date')[:5]

class AboutView(generic.ListView):
    template_name = 'pages/about.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self): 
        return Question.objects.order_by('-pub_date')[:5]

class ServicesView(generic.ListView):
    template_name = 'pages/services.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self): 
        return Question.objects.order_by('-pub_date')[:5]

class ProductsView(generic.ListView):
    template_name = 'pages/products.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self): 
        return Question.objects.order_by('-pub_date')[:5]
