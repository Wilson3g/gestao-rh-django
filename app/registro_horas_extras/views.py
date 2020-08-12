from django.shortcuts import render
from django.views.generic import ListView
from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    models = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresas
        print(empresa_logada)
        return RegistroHoraExtra.objects.filter(funcionario__empresas=empresa_logada)
