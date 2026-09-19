from django.urls import path
from .views import FuncionarioCreateView, FuncionarioDeleteView, FuncionarioUpdateView, ListaFuncionarios, IndexTemplateView
# from django.views.generic import TemplateView

# Importamos a função index() definida no arquivo views.py
from . import views

app_name = 'website'
# urlpatterns contém a lista de roteamentos de URLs

urlpatterns = [
    # GET /
    # path('', views.index, name='index'),

    path('template/', IndexTemplateView.as_view(), name='template'),

    path('funcionarios-lista/', ListaFuncionarios.as_view(), name='lista_funcionarios'),

    path('funcionario/<int:pk>/', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),

    path('funcionario/excluir/<int:pk>/', FuncionarioDeleteView.as_view(), name='deleta_funcionario'),

    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),

    # path('funcionarios/', views.index, name='index'),

]

