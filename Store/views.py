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

def categorias(request, id):
    categ = Categoria.objects.filter(departamento_id=id)
    depto = Departamento.objects.get(id = id)
    context = {'categorias':categ, 'departamento': depto }
    return render(request, 'categorias.html', context)           

def produtos(request, id):
    prod = Produto.objects.filter(categoria_id=id)
    categ = Categoria.objects.get(id = id)
    context = {'produtos':prod, 'categoria':categ}
    return render(request, 'produtos.html', context)

def produto_detalhe(request, id):
    detalhes = Produto.objects.get(id = id)
    context = {'produto':detalhes}
    return render(request, 'produto_detalhe.html', context)        

