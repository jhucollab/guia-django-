from django.urls import path 
from .import views                                                  #conectar vistas
urlpatterns = [
    path("Energia/", views.listado_energia,
         name= "listado_energia"),
    path("Particula/", views.listado_particulas,
         name = "listado_particula"),
]