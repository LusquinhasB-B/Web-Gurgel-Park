from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

# Create your views here.
def home(request):
    return render(request, "home.html")


def cadastro(request):
    if request.method == "POST":
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if not usuario:
            return HttpResponse("Usuario não informado")
        elif not email:
            return HttpResponse("email não informado")
        elif not senha:
            return HttpResponse("Senha não inserida")

    # Traz do banco de dados do proprio django se existe um usuairo com o mesmo nome
        user = User.objects.filter(username=usuario).first()
        if user:
            return HttpResponse('Já existe um usuário com esse Username')
        
    #Pede para criar com outro nome
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()

        return HttpResponse("Usuário cadastrado com sucesso!")

    return render(request, 'cadastro.html')
def login(request):
    
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        usuario = request.POST.get('username')
        senha = request.POST.get('senha') 

        user = authenticate(username=usuario, password=senha)

        if user:
            login_django(request, user)
            return redirect(request, "pagina.html")
        else:
            return HttpResponse("Usuario ou senhas inválidos")
        
def paginaPrincipal(request):
    if request.user.is_authenticated:
        return render(request, 'pagina.html')
    return HttpResponse("Precisa estar LOGADO PARA acessar a página!")