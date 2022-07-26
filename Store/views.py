from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento

# Create your views here.

def index(request):
    meu_nome = 'Charlie Head Horse'
    sexo = 'F'
    context = {'nome': meu_nome, 'artigo': 'o' if sexo == 'M' else 'a'}
    return render(request, 'index.html', context)

def teste(request):
    depto = Departamento.objects.all()
    context = {'departamentos':depto}
    return render(request, 'teste.html', context)
        

