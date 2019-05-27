from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from .models import Question
from django.shortcuts import get_object_or_404, render
from django.utils.html import escape
from django.urls import reverse

def index(request):
    #Next 3 lines , original code from the tutorial
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    question_list = Question.objects.order_by('pub_date')
    #if there is no  template then use this rendering logic , where everything is defined in the code
    #output = ', '.join(q.question_text for q in question_list)
    #print("The value for output is %s" %output)
    #return HttpResponse(output)
    context = {'latest_question_list' : question_list}
    return render(request,'polls/index.html',context)

def details(request,question_id):
    #return HttpResponse("(Under Implementation)Hello thanks for asking about a question ,this is the question id you asked for %s" % question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    print("Moving after exception")
    #context is the one which connects 'question' in view to the 'question' in template
    context = {'question' : question}
    return render(request,'polls/question_detail.html', context)

def results(request,question_id):
    question=Question.objects.get(pk=question_id)
    return HttpResponse("The question text is   %s" % question.question_text)

def vote(request,question_id):
    #return HttpResponse("(Under implementation ) You are looking at the no of votes for the question no :  %s" % question_id)
    question=get_object_or_404(Question , pk=question_id)
    print(request.POST)
    
    #Now we got a reference to the choice object
    choice = question.choice_set.get(pk=request.POST.get('choice'))
    choice.votes = choice.votes + 1 
    choice.save()

    #Now comes the redirection logic
    return HttpResponseRedirect(reverse('results', args=[question.id]))
