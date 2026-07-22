from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def ver_produto(request):
    if request.method == "GET":
        nome = 'Caio'
        return render(request, 'ver_produto.html' , {'nome': 'nome'})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

    pessoas = Pessoa.objects.all()
    print(pessoas)

    return HttpResponse(pessoas)

def inserir_produto(request):
    return HttpResponse('Estou no inserir')
