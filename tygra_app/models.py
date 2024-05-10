from django.db import models

# Create your models here.


class Promocao(models.Model):
    data_inicio = models.CharField(max_length=50)
    data_fim = models.CharField(max_length=50)
    valor = models.CharField(max_length=100)    

    class Meta: 
        verbose_name_plural = 'Promoções'
    
    def __str__(self):
        return f"Data de Início: {self.data_inicio}, Data de Fim: {self.data_fim}, Valor: {self.valor}"

class Produto(models.Model):
    promocao = models.ForeignKey(Promocao, on_delete=models.SET_NULL, null = True, blank = True)
    text = models.CharField(max_length=200)
    data_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text