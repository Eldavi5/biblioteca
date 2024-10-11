from django.urls import path
from .utils import contar_palabras, ordenar_lista

urlpatterns = [
    path("contar_palabras/", contar_palabras, name="contar_palabras"),
    path("ordenar_lista/", ordenar_lista, name="ordenar_lista"),
]
