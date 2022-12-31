from django.shortcuts import render, get_object_or_404
from .models import Receita
from pessoas.models import Pessoa


def index(request):
    receitas = Receita.objects.filter(publicada=True).order_by('-data_receita')

    dados = {
        'receitas' : receitas
    }
    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
     
    dados = {
        'receita' : receita,
    }
    return render(request, 'receitas/receita.html', dados)

def buscar(request):  
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        # if buscar:
        #     lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    lista_receitas = Receita.objects.filter(publicada=True, nome_receita__icontains=nome_a_buscar).order_by('-data_receita')    
    
    dados = {
        'receitas': lista_receitas,
    }

    return render(request, 'receitas/buscar.html', dados)