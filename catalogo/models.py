from django.db import models

class Bolo(models.Model):
    nome = models.CharField(max_length=255)
    sabor = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class Bolo(models.Model):
    nome = models.CharField(max_length=100)
    sabor = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='bolos/', null=True, blank=True)

    def __str__(self):
        return self.nome

