from django.db import models


class Produto (models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits = 6, decimal_places = 2)
    descricao = models.TextField()
    data_cadastro = models.DateField(auto_now_add=True)
    mais_Detalhe = models.TextField()
    sub_categoria = models.ForeignKey("SubCategoria", on_delete=models.CASCADE)
    promocao = models.ForeignKey("Promocao", on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__ (self):
        return self.nome
    
class Imagem (models.Model):
    nome_imagem = models.CharField(max_length=50)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.nome_imagem

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)
    
    def __str__ (self):
        return self.nome_categoria

class SubCategoria(models.Model):
    nome_sub = models.CharField(max_length=20)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.nome_sub 
class Promocao(models.Model):
    valor = models.DecimalField(max_digits = 6, decimal_places = 2)
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()

    def __str__ (self):
        return self.valor 

    
class Cliente (models.Model):
    nome_completo = models.CharField(max_length=100)
    data_cadastroUser = models.DateField(auto_now_add=True)
    data_nasc = models.DateTimeField()
    cpf = models.CharField(max_length=14)
    endereço = models.ForeignKey("Endereco", on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    
class Carrinho_Produto(models.Model):
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    user = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    quantidade = models.CharField(max_length=20)

    def __str__(self):
        return self.user

class Carrinho (models.Model):
    user = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user
    
class Endereco(models.Model):
    cep = models.CharField(max_length=10)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=50)

    def __str__(self):
        return self.cep 
    
class Referencia(models.Model):
    referencia = models.TextField()
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE)

    def __str__(self):
        return self.referencia
    
class Pais(models.Model):
    nome_pais = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_pais
    
class Estado (models.Model):
    nome_estado = models.CharField(max_length=20)
    pais = models.ForeignKey("Pais", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_estado
    
class Cidade (models.Model):
    nome_cidade = models.CharField(max_length=20)
    estado = models.ForeignKey("Estado", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_cidade
    
class Bairro (models.Model):
    nome_bairro = models.CharField(max_length=20)
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_bairro
    
class NomeLogradouro (models.Model):
    nome_logradouro = models.CharField(max_length=20)
    bairro = models.ForeignKey("Bairro", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_logradouro
