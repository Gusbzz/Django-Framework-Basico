from django.shortcuts import render
from django.http import HttpResponse

def ver_produto(request):
    if request.method == "GET":
        nome = 'Caio'
        return render(request, 'ver_produto.html' , {'nome': 'nome'})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

def inserir_produto(request):
    return HttpResponse('Estou no inserir')
