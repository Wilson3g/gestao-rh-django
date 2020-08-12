from django.db import models
from app.funcionarios.models import Funcionario
from django.shortcuts import reverse


class Documento(models.Model):
    descricao = models.CharField(max_length=100, help_text='Descricao do departamento')
    proprietario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.proprietario.id])

    def __str__(self):
        return self.descricao
