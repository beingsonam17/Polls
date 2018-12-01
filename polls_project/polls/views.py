from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse,reverse_lazy
from django.views import generic
import datetime
from django.utils import timezone
from .models import Choice, Question
from django.views.generic import (ListView,DetailView,TemplateView,
                    CreateView,UpdateView,DeleteView)
from . import models

class IndexView(ListView):
    
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



class DetailView(DetailView):
    
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
   
class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class ThanksPage(TemplateView):
    template_name = 'polls/thanks.html'
    
class HomePage(TemplateView):
    template_name = 'polls/index.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        return super().get(request, *args, **kwargs)

class QuestionsCreateView(CreateView):
    fields = ('question_text',)
    model = models.Question
    
   

class QuestionsUpdateView(UpdateView):
    fields = ('question_text',)
    model = models.Question

class QuestionsDeleteView(DeleteView):
    model = models.Question
    success_url = reverse_lazy("polls:index")
    def goback(request):
        return HttpResponseRedirect(reverse("index"))
    
class ChoiceCreateView(CreateView):
    fields = ('question','choice_text','votes')
    model = models.Choice


    


