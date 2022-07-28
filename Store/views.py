from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento, Categoria, Produto 


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

def departamentos(request):
    depto = Departamento.objects.all()
    context = {'departamentos':depto}
    return render(request, 'departamentos.html', context)

def categorias(request):
    categ = Categoria.objects.all()
    context = {'categorias':categ}
    return render(request, 'categorias.html', context)           

def produtos(request):
    prod = Produto.objects.all()
    context = {'produtos':prod}
    return render(request, 'produtos.html', context)        

