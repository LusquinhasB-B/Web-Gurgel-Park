from django.urls import path
from . import views 

urlpatterns =[
    path('pagina/', views.paginaPrincipal, name='pagina'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('sistema/', views.sistema, name='sistema'),
    path('projeto/', views.projeto, name='projeto'),
    path('', views.home, name="home")
]