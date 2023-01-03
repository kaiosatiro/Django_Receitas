from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


def cadastro(request):
    """Esse metodo entrega a pagina de cadastro e tambem recebe as requisições para cadastro """ 
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request,'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request,'O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Usuário já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request,'Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')


def login(request):
    """Esse metodo realiza o login"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request,'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
        messages.error(request, 'Usuário ou senha inválido')
    return render(request, 'usuarios/login.html')


def logout(request):
    """Esse metodo realiza o logout"""
    auth.logout(request)
    return redirect('index')


def campo_vazio(campo):
    """Essa funcao valida campos vaioz em formularios"""
    return not campo.strip()


def senhas_nao_sao_iguais(senha, senha2):
    """Essa funcao valida se as duas senhas fornecidas no cadastro são iguais"""
    return senha != senha2

