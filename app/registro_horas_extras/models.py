from django.db import models
from app.funcionarios.models import Funcionario
from django.urls import reverse


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=70, help_text='Motivo da extra')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse('edit_hora_extra', args=[self.id])
