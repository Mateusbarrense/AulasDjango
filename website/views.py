from django.shortcuts import render
from OlaMundo.models import Funcionario
from django.views.generic.list import ListView
from django.views.generic import TemplateView



# Create your views here.


# def index(request):
#     return lista_funcionarios(request)

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"

def lista_funcionarios(request):
    # Buscar os funcionarios
    funcionarios = Funcionario.objects.all()

    # Incluir no contexto
    contexto = {'funcionarios': funcionarios}

    # Retornar o templete para listar os funcionarios
    return render(request, "website/funcionarios.html", contexto)


class ListaFuncionarios(ListView):
    template_name = "website/funcionarios-lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

