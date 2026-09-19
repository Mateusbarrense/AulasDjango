from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from OlaMundo.models import Funcionario
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import TemplateView, CreateView



# Create your views here.


# def index(request):
#     return lista_funcionarios(request)

class IndexTemplateView(TemplateView):
    template_name = "website/template.html"

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

class FuncionarioUpdateView(UpdateView):
    template_name = 'website/atualiza.html'
    model = Funcionario
    fields = [
        'nome',
        'sobrenome',
        'cpf',
        'tempo_de_servico',
        'remuneracao'
    ]

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")

class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        # Modelo base
        model = Funcionario
        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'remuneracao'
            ]
        # Campos que não estarão no form
        exclude = [
        'tempo_de_servico'
        ]

class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")    
