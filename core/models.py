from django.db import models

# Create your models here.


class Bicicleta(models.Model):
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    valor = models.DecimalField()
    nome_comparador = models.CharField(max_length=100)
    nome_loja = models.CharField(max_length=100)
    data_compra = models.DateField()

    def __str__(self):
        return self.modelo