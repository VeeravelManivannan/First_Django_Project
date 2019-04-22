from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    #Next 3 lines , original code from the tutorial
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    question_list = Question.objects.order_by('pub_date')
    output = ', '.join(q.question_text for q in question_list)
    print("The value for output is %s" %output)
    return HttpResponse(output)

def details(request,question_id):
    return HttpResponse("(Under Implementation)Hello thanks for asking about a question ,this is the question id you asked for %s" % question_id)

def results(request,question_id):
    return HttpResponse("(Under implementation)You are now looking at the results of the question no :  %s" % question_id)

def vote(request,question_id):
    return HttpResponse("(Under implementation ) You are looking at the no of votes for the question no :  %s" % question_id)
