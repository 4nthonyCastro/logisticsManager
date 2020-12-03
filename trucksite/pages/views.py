from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.views import generic
from django.utils import timezone
from django.urls import reverse
from django.template import loader

from .models import Question, Choice

# Create your views here.
# def index(request):
#    template = loader.get_template('pages/index.html')
#    return HttpResponse(template.render({},request))

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

#def about(request):
#    template = loader.get_template('pages/about.html')
#    return render(request, 'pages/about.html', {})
    # return HttpResponse(template.render({},request))
