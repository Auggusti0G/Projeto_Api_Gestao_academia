#----------------------------------------
#----Criacção do model de instrutores----
#----------------------------------------

from django.db import models

class Instrutor(models.Model):

    nome = models.CharField(max_length=100)

    especialidade = models.CharField(max_length=100)

    telefone = models.CharField(max_length=20)

    email = models.EmailField()

    salario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'Instrutor'
        verbose_name_plural = 'Instrutores'

    def __str__(self):
        return self.nome