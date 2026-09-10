from django.shortcuts import render
from OlaMundo.models import Funcionario
# Create your views here.


def index(request):
    return lista_funcionarios(request)



def lista_funcionarios(request):
    # Buscar os funcionarios
    funcionarios = Funcionario.objects.all()

    # Incluir no contexto
    contexto = {'funcionarios': funcionarios}

    # Retornar o templete para listar os funcionarios
    return render(request, "website/funcionarios.html", contexto)