from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def details(request,question_id):
    return HttpResponse("Hello thanks for asking about a question ,this is the question id you asked for %s" % question_id)
