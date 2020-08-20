from django.db import models
from django.contrib.auth.models import User
from app.departamentos.models import Departamento
from app.empresas.models import Empresa
from django.urls import reverse
from django.db.models import Sum

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do funcionario')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Departamentos = models.ManyToManyField(Departamento)
    empresas = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('list_funcionarios')

    @property
    def total_horas_extras(self):
        return self.registrohoraextra_set.all().aggregate(
            Sum('horas')
        )['horas__sum']
