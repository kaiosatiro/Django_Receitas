from django.shortcuts import render, redirect
from receitas.models import Receita
from django.core.paginator import Paginator

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        paginator = Paginator(receitas, 6)
        page = request.GET.get('page')
        receitas_p_pg = paginator.get_page(page)
        
        dados = { 
            'receitas' : receitas_p_pg
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')
