from django import forms

from tygra_app.models import Categoria, Imagem, Produto, SubCategoria

class ProdutoForm (forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','descricao','mais_Detalhe','sub_categoria', 'promocao']
        labels = {'preco':"Preço"}
        
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update(
            {'placeholder':'Nome do produto',
            'class' : 'form-control'}
        )
        self.fields['preco'].widget.attrs.update(
            {'placeholder':'Preço',
            'class' : 'form-control'}
        )
        self.fields['descricao'].widget.attrs.update(
            {'placeholder':'Descrição',
            'class' : 'form-control'}
        )
        self.fields['mais_Detalhe'].widget.attrs.update(
            {'placeholder':'Detalhe do produto',
            'class' : 'form-control'}
        )
        self.fields['sub_categoria'].widget.attrs.update(
            {'placeholder':'sub_categoria',
            'class' : 'form-control'}
        )
        self.fields['promocao'].widget.attrs.update(
            {'placeholder':'Promoção',
            'class' : 'form-control'}
        )

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['nome_imagem']     
    
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_imagem'].widget.attrs.update(
            {'placeholder':'Nome da imagem',
            'class' : 'form-control'}
        )

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome_categoria']     
    
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_categoria'].widget.attrs.update(
            {'placeholder':'Nome da categoria',
            'class' : 'form-control'}
        )

class SubCategoriaForm(forms.ModelForm):
    class Meta:
        model = SubCategoria
        fields = ['nome_sub', 'categoria']     
    
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_sub'].widget.attrs.update(
            {'placeholder':'Nome da sub categoria',
            'class' : 'form-control'}
        )
        self.fields['categoria'].widget.attrs.update(
            {'placeholder':'categoria',
            'class' : 'form-control'}
        )