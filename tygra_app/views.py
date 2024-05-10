from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from tygra_app.forms import CategoriaForm, ProdutoForm, SubCategoriaForm
from tygra_app.models import Imagem

def home (request):   
    return render(request, 'index.html')

def add_produtos(request):
    if request.method == "GET":
        form = ProdutoForm()
    else:
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form = form.save()
            imagem = Imagem.objects.create(name = request.POST["imagem"], id_produto = form.id)
            imagem.save()
            return HttpResponseRedirect(reverse('home'))
    context = {'form':form}
    return render(request,'add_produto.html',context)

def add_categorias(request):
    if request.method == "GET":
        form = CategoriaForm()
    else:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')      
    context = {'form': form}

    return render(request, 'add_categorias.html', context)

def add_subcategorias(request):
    if request.method == "GET":
        form = SubCategoriaForm()
    else:
        form = SubCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')      
    context = {'form': form}

    return render(request, 'add_subcategorias.html', context)
