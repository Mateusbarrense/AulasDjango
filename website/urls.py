from django.urls import path
from .views import ListaFuncionarios, IndexTemplateView
from django.views.generic import TemplateView

# Importamos a função index() definida no arquivo views.py
from . import views

app_name = 'website'
# urlpatterns contém a lista de roteamentos de URLs

urlpatterns = [
    # GET /
    # path('', views.index, name='index'),

    path('', IndexTemplateView.as_view(), name='index'),

    path('funcionarios-lista/', ListaFuncionarios.as_view(), name='lista_funcionarios'),

    # path('funcionarios/', views.index, name='index'),

]

