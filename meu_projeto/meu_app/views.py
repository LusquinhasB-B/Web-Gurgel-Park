from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    else:
        irPrincipal = request.POST.get('irPagina')
        irLogin = request.POST.get('irLogin')
        irCadastro = request.POST.get('irCadastro')

        if irPrincipal:
            return redirect('/auth/pagina/')
        if irLogin:
            return redirect('/auth/login/')
        if irCadastro:
            return redirect('/auth/cadastro/')



#----------------------Método Cadastro---------------------#

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if not usuario:
            return HttpResponse("Usuario não informado")
        elif not email:
            return HttpResponse("email não informado")
        elif not senha:
            return HttpResponse("Senha não inserida")

        # Se ja existe um usuario com o mesmo nome
        user = User.objects.filter(username=usuario).first()

        if user:
            return HttpResponse('Já existe um usuário com esse Username')
        
        #Pede para criar com outro nome
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()

        #redireciona o usuario a até a pagina de login
        return redirect("/auth/login/")

#----------------------Método Login---------------------#

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')  
    else:
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')  

        validacao = authenticate(username=usuario, password=senha)

        if validacao:
            login_django(request, validacao)
            return redirect("/auth/pagina/")
        else:
            return HttpResponse("<h2>Usuario ou senhas inválidos </h2>"
            "<br> "
            "<a href='/auth/login/'>Clique aqui para voltar a area de Login</a>")
        

#----------------------Página Principal---------------------#

def paginaPrincipal(request):
    if request.user.is_authenticated:
        return render(request, 'pagina.html')
    return HttpResponse("Precisa estar LOGADO PARA acessar a página!"
    "<br>"
    "<a href='/auth/login/'>Clique aqui para ir a pagina de login </a>" \
    "<br>" \
    "<a href='/auth/cadastro/'>Ou clique aqui para ir a pagina de cadastro</a>" \
    "")