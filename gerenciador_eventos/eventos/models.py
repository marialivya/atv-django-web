from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Participante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes')

    def __str__(self):
        return f"{self.nome} ({self.email})"
