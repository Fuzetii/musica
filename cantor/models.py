from django.db import models
from estilo.models import Estilos

class Cantores(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    estilo = models.ForeignKey(Estilos, on_delete=models.CASCADE, default='POP')
                               
    def __str__(self):
        return self.nome
