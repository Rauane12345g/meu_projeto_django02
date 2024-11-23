
# Create your models here.

from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.preco <= 0:
            raise ValueError("O preço deve ser maior que zero!")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
