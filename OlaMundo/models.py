from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(
    max_length=255,
    null=False,
    blank=False
)
    sobrenome = models.CharField(
    max_length=255,
    default=' ',
    null=False,
    blank=False
)
    cpf = models.CharField(
    max_length=14,
    default='111.111.111-11',
    null=False,
    blank=False
)
    tempo_de_servico = models.IntegerField(
    default=0,
    null=False,
    blank=False
)
    remuneracao = models.DecimalField(
    max_digits=8,
    default=0.00,
    decimal_places=2,
    null=False,
    blank=False
)
objetos = models.Manager()