from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>blog</h1>')

# Create your views here.
