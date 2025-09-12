from django.shortcuts import render
from .models import Filme

# Create your views here.
def listar_filmes(request):
    filmes = Filme.objects.all() 
    
    return render(request,'filmes/lista.html', {"filmes": filmes})