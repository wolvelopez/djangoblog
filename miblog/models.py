from django.db import models
from django.contrib.auth.models import User


class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    etiquetas = models.CharField(max_length=100)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    comentario_texto = models.CharField(max_length=200)
    comentario_fecha = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(User)
    entrada = models.ForeignKey(Entrada)

    def __str__(self):
        return self.comentario_texto