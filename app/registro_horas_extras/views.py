from django.shortcuts import render
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView
)
from .models import RegistroHoraExtra
from django.urls import reverse_lazy


class HoraExtraList(ListView):
    models = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresas
        return RegistroHoraExtra.objects.filter(funcionario__empresas=empresa_logada)


class HoraExtraUpdate(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra

    success_url = reverse_lazy('list_hora_extra')
