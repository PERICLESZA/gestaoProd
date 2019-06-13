from django.db import models


# Create your models here.

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    hora = models.TimeField()
    imagem = models.ImageField(upload_to='produto_img', null=True, blank=True)

    def __str__(self):
        return self.nome

