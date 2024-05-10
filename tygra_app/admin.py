from django.contrib import admin
from tygra_app.models import Bairro, Carrinho, Carrinho_Produto, Categoria, Cidade, Cliente, Endereco, Estado, Imagem, NomeLogradouro, Pais, Produto, Promocao, Referencia, SubCategoria

admin.site.register(Produto)
admin.site.register(Imagem)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Promocao)
admin.site.register(Cliente)
admin.site.register(Carrinho_Produto)
admin.site.register(Carrinho)
admin.site.register(Endereco)
admin.site.register(Referencia)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(NomeLogradouro)
