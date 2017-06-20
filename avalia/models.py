from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Evento(models.Model):
    administrador = models.ForeignKey(User, null = False)
    nome = models.CharField('nome',max_length=200, null = True)
    def __str__(self):
        return '{}'.format(self.nome)



class Artigo(models.Model):
    nome = models.CharField('nome',max_length=200, null = False)
    evento = models.ForeignKey('Evento',max_length=200 )
    autor = models.ForeignKey(User, null = False)
    nota = models.FloatField('nota', null = False, default=0)

    def __str__(self):
        return '{}'.format(self.nome,self.nota)



class Avaliacao(models.Model):
    avaliador = models.ForeignKey(User, null = False)
    artigo = models.ForeignKey('Artigo', null = False)
    qualidade = models.FloatField('qualidade', default=0)
    inovacao = models.FloatField('inovacao', default=0)
    resultados = models.FloatField('resultados', default=0)
    metodologia = models.FloatField('metodologia', default=0)
    adequacao = models.FloatField('adequacao', default=0)

    def __str__(self):
        return '{}'.format(self.artigo)
