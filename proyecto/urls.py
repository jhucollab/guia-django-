from django.urls import path
from . import views

urlpatterns = [
    path('energia/', views.listado_energia, name='listado_energia'),
    path('particula/', views.listado_particulas, name='listado_particula'),
]
