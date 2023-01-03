from ..models import Receita
from django.shortcuts import render


def busca(request):  
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        # if buscar:
        #     lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    lista_receitas = Receita.objects.filter(publicada=True, nome_receita__icontains=nome_a_buscar).order_by('-data_receita')    
    
    dados = {
        'receitas': lista_receitas,
    }

    return render(request, 'receitas/buscar.html', dados)