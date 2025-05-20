from django.urls import path
from . import views 

urlpatterns =[
    #telas principais
    path('pagina/', views.paginaPrincipal, name='pagina'),
    path('sistema/', views.sistema, name='sistema'),
    path('projeto/', views.projeto, name='projeto'),
    path('conta/', views.conta, name='conta'),
    #Telas de cadastro
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    #telas adcionais de funções
    path('redefinir_senha/', views.redefinir_senha, name='redefinir_senha'),
    path('conta/atualizar_email/', views.atualizar_email, name="atualizar_email"),
    path('deslogar', views.sair, name='deslogar')
    # path('', views.home, name="home")
]
