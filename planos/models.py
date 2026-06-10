#----------------------------
#-----models de planos-------
#----------------------------

from django.db import models

class Plano(models.Model):

    nome = models.CharField(max_length=100)

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    duracao = models.IntegerField()

    descricao = models.CharField(max_length=200)

    modalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome