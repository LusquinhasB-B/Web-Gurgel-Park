from django.urls import path
from . import views 

urlpatterns =[
    path('', views.paginaPrincipal, name='paginaPrincipal'),
    path('', views.home, name='home'),
]