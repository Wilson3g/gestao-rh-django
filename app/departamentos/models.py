from django.db import models
from app.empresas.models import Empresa
from django.urls import reverse


class Departamento(models.Model):
    nome = models.CharField(max_length=70, help_text='Nome do departamento')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_departamentos')
