from django import forms
from django.contrib.auth.models import User

class LoginForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {'password': forms.PasswordInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder':"Nome de Usuario", 'class': 'form-control my-2 p-2'})
        self.fields['password'].widget.attrs.update(
            {'placeholder':"Senha", 'class': 'form-control my-2 p-2'})


class cadastroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password","email","first_name","last_name"]
        widgets = {"email":forms.EmailInput(),"password":forms.PasswordInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder':"Nome de Usuario", 'class': 'form-control my-2 p-2'})
        self.fields['password'].widget.attrs.update(
            {'placeholder':"Senha", 'class': 'form-control my-2 p-2'})
        self.fields['email'].widget.attrs.update(
            {'placeholder':"Email", 'class': 'form-control my-2 p-2'})
        self.fields['first_name'].widget.attrs.update(
            {'placeholder':"Prenome", 'class': 'form-control my-2 p-2'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder':"Sobrenome", 'class': 'form-control my-2 p-2'})
        


class RemoverForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {'password': forms.PasswordInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder':"Nome de Usuario", 'class': 'form-control my-2 p-2'})
        self.fields['password'].widget.attrs.update(
            {'placeholder':"Senha", 'class': 'form-control my-2 p-2'})