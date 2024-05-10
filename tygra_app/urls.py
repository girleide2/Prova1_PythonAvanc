from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'), 
    path('add_produtos/', views.add_produtos, name = 'add_produtos'), 
    path('add_categorias/', views.add_categorias, name = 'add_categorias'), 
    path('add_subcategorias/', views.add_subcategorias, name = 'add_subcategorias'),
]