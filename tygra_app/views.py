from django.shortcuts import render
from .models import Produto, Categoria, Imagem, Promocao, SubCategoria
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .forms import LoginForm, cadastroForm, RemoverForm
from django.contrib.auth.hashers import make_password


def home (request):   
    return render(request, 'index.html')

def produto(request):
    produtos = Produto.objects.order_by('date_added')
    context = {'produtos': produtos}
    return render(request, context)

def categoria(request):
    categorias = Categoria.objects.order_by('date_added')
    context = {'categorias': categorias}
    return render(request, context)

def imagem(request):
    imagens = Imagem.objects.order_by('date_added')
    context = {'imagens': imagens}
    return render(request, context)

def promocao(request):
    promocoes = Promocao.objects.order_by('date_added')
    context = {'promocoes': promocoes}
    return render(request, context)

def subCategoria(request):
    subCategorias = SubCategoria.objects.order_by('date_added')
    context = {'subCategorias': subCategorias}
    return render(request, context)


def login(request):
    form_login = LoginForm()
    contexto = {"form_login": form_login}
    if request.method=="POST":
        user = authenticate(username=request.POST.get("username"),password=request.POST.get("password"))
        if user:
            auth_login(request,user)
            return HttpResponseRedirect(reverse("cadastro"))

    return render(request,"login.html",contexto)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("home"))


def cadastro(request):
    if request.method=="POST":
        form_cadastro = cadastroForm(request.POST)
        if form_cadastro.is_valid():
            if request.POST.get("password")!=request.POST.get("confirmacao"):
                form_cadastro.add_error("password","As senhas devem ser iguais")
            else:
                form_cadastro = form_cadastro.save(commit=False)
                form_cadastro.password = make_password(form_cadastro.password)
                form_cadastro.save()
                return HttpResponseRedirect(reverse("home"))

    form_cadastro = cadastroForm()
    contexto = {"form_cadastro":form_cadastro}
    return render(request,"cadastro.html",contexto)

def remover(request):
    form_remover = RemoverForm()
    contexto = {"form_remover": form_remover}
    if request.method=="POST":
        user = authenticate(username=request.POST.get("username"),password=request.POST.get("password"))
        if user:
            user.delete()
            return HttpResponseRedirect(reverse("home"))

    return render(request,"remover.html",contexto)