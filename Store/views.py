from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HTTPResponse('Hello World!')

def teste(request):
    return HttpResponse('Minha página de teste')
        

