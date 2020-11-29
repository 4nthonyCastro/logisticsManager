# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

from django.template import loader

# [Views for Polls]
# ===================
#       Function:
#           - Views can read records from a database, utilize a template system, or generate output in PDF, XML, and ZIP files.
#             All Django wants is that HttpResponse or an Exception. 

# [Index View]
# ===================
#       Function:
#           - Using the render() funtion, it takes the request object as its first argument, 
#             a template name as its second argument, and a dictionary as its option third argument 
#       Return:
#           - Question.objects.filter(pub_date__lte=timezone.now()), returns a queryset containing
#             Questions whose pub_date is less than or equal to - that is, earlier than or equal to
#             timezone.now
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# [Detail View]
# ===================
#       Function: 
#           - The details view raises the Http404 exception if a question with the requested ID doesn't exist.
#             We use a Django short cut to get question or throw Http404 exception
#       Return: 
#           - Returns valid question or 404 error for not existing.
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# [Results View]
# ==================
#       Function: 
#           -
#       Return:
#           -
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# [Vote View]
# ==================
#       Function:   
#           -
#       Return: 
#           -
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting from:
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Return an HttpResponseRedirect after successful dealing with POST data. 
        # This prevents data from being posted twice, when a user hits the Back button. 
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
