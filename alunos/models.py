#------------------------------------
#--------models de aluno criado------
#------------------------------------

from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome