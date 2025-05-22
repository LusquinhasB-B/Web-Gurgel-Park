from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as login_django
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .forms import  EmailUpdateFormulario

#------------------Tela Home---------------------#

# def home(request):
#     #Renderiza a página HTML
#     if request.method == "GET":
#         return render(request, "home.html") 
#     #Através dos métodos GET e POST, ele realiza o método caso determiniado botão for pressionado
#     else:
#         irPrincipal = request.POST.get('irPagina')
#         irLogin = request.POST.get('irLogin')
#         irCadastro = request.POST.get('irCadastro')

#         if irPrincipal:
#             return redirect('/auth/pagina/')
#         if irLogin:
#             return redirect('/auth/login/')
#         if irCadastro:
#             return redirect('/auth/cadastro/')



# #----------------------Método Cadastro---------------------#

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        #---------------Ir para outras telas---------------#
        irPrincipal = request.POST.get('irPagina')
        irLogin = request.POST.get('irLogin')
        if irPrincipal:
            return redirect('/GurgelPark/pagina/')
        if irLogin:
            return redirect('/GurgelPark/login/')
    
        # Se os campos não forem preenchidos
        if not usuario:
            return render(request, 'erro.html', {
                'titulo': 'Erro de cadastro',
                'mensagem': 'USUÁRIO NÃO INFORMADO!',
                'link': '/GurgelPark/cadastro/'
            })
        elif not email:
            return render(request, 'erro.html', {
                'titulo': 'Erro de cadastro',
                'mensagem': 'EMAIL NÃO INFORMADO!',
                'link': '/GurgelPark/cadastro/'
            })

        elif not senha:
            return render(request, 'erro.html', {
                'titulo': 'Erro de cadastro',
                'mensagem': 'SENHA NÃO INFORMADA!',
                'link': '/GurgelPark/cadastro/'
            })
        
        # Se ja existe um usuario com o mesmo nome
        user = User.objects.filter(username=usuario).first() 
        if user:
            return render(request, 'erro.html', {
                'titulo': 'Usuário já existente',
                'mensagem': 'Utilize outro nickname!',
                'link': '/GurgelPark/cadastro/'
            })

        
        #Pede para criar com outro nome
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()

        #redireciona o usuario a até a pagina de login
        return redirect("/GurgelPark/login/")

#----------------------Método Login---------------------#

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')  
    else:
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')  

        #---------------Ir para outras telas---------------#
        irPrincipal = request.POST.get('irPagina')
        irCadastro = request.POST.get('irCadastro')

        if irPrincipal:
            return redirect('/GurgelPark/pagina/')
        if irCadastro:
            return redirect('/GurgelPark/cadastro/')

        if not usuario:
            return render(request, 'erro.html', {
                'titulo': 'Erro de Login',
                'mensagem': 'Usuário não inserido!',
                'link': '/GurgelPark/login/'
            })
        if not senha:
            return render(request, 'erro.html', {
                'titulo': 'Erro de Login',
                'mensagem': 'Senha não inserida!',
                'link': '/GurgelPark/login/'
            })
        
        validacao = authenticate(username=usuario, password=senha)

        if validacao:
            login_django(request, validacao)
            return redirect("/GurgelPark/pagina/")
        else:
            return render(request, 'erro.html', {
                'titulo': 'Erro de Login',
                'mensagem': 'Usuário ou senha inválidos!',
                'link': '/GurgelPark/login/'
            })



#----------------------REDEFINIR SENHA---------------------#

def redefinir_senha(request):
    if request.method == "GET":
        return render(request, 'redefinir_senha.html')
    voltar = request.POST.get('voltar')
    usuario = request.POST.get('username')
    nova_senha = request.POST.get('nova_senha')
    teste = request.POST.get('teste')

    if voltar:
        return redirect('/GurgelPark/login/')

    if not usuario:
        return render(request, 'erro.html', {
        'titulo': 'Erro ao redefinir senha!',
        'mensagem': 'Campo "Usuário" não inserido!',
        'link': '/GurgelPark/redefinir_senha/'
        })
    if not nova_senha:
        return render(request, 'erro.html', {
        'titulo': 'Erro ao redefinir senha!',
        'mensagem': 'Campo "Nova senha" não inserido!',
        'link': '/GurgelPark/redefinir_senha/'
        })

    user = User.objects.filter(username=usuario).first()


    if user:
        user.password = make_password(nova_senha)
        user.save()
        return redirect('login')
    
    else:
        return render(request, 'erro.html', {
        'titulo': 'Erro ao redefinir senha!',
        'mensagem': 'Usuário não encontrado!',
        'link': '/GurgelPark/login/'
})


#----------------------Página Principal---------------------#
@login_required
def atualizar_email(request):
    if request.method == 'POST':
        form = EmailUpdateFormulario(request.POST)
        if form.is_valid():
            novo_email = form.cleaned_data['novo_email']
            request.user.email = novo_email
            request.user.save()
            return redirect('conta')  # Redireciona para tela da conta
    else:
        form = EmailUpdateFormulario(initial={'novo_email': request.user.email})

    return render(request, 'atualizar_email.html', {'form': form})

#----------------------Página Principal---------------------#


def paginaPrincipal(request):
    if request.user.is_authenticated:
        return render(request, 'pagina.html')
    return render(request, 'erro.html', {
        'titulo': 'Erro de acesso! ',
        'mensagem': 'Entre ou cadastra-se para ter acesso!',
        'link': '/GurgelPark/login/'
})


#----------------------Página Sistema---------------------#

def sistema(request):
    if request.user.is_authenticated:
        return render(request, 'sistema.html')
    return render(request, 'erro.html', {
        'titulo': 'Erro de acesso!',
        'mensagem': 'Entre ou cadastra-se para ter acesso!',
        'link': '/GurgelPark/login/'
})


#----------------------Página Projeto---------------------#

def projeto(request):
    if request.user.is_authenticated:
        return render(request, 'projeto.html')
    return render(request, 'erro.html', {
        'titulo': 'Erro de acesso!',
        'mensagem': ' Entre ou cadastra-se para ter acesso!',
        'link': '/GurgelPark/login/'
})

#-------------------------Deslogar da conta---------------#

def conta(request):
    if request.user.is_authenticated:
        return render(request, 'conta.html', {'user': request.user})
    else:
        return render(request, 'erro.html', {
            'titulo': 'Erro de acesso!',
            'mensagem': ' Entre ou cadastra-se para ter acesso!',
            'link': '/GurgelPark/login/'
        })

#-------------------------Deslogar da conta---------------#
@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect('login/')

#------------------------Erros------------------------

