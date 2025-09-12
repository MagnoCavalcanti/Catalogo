from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_filmes, name='listar_filmes'),
]