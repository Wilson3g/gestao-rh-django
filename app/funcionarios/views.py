from django.http import HttpResponse
from django.views.generic import ListView, UpdateView
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresas
        queryset = Funcionario.objects.filter(empresas=empresa_logada)
        return queryset


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']