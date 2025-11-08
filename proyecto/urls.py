from django.urls import path
from . import views

urlpatterns = [
    path('energia/', views.listado_energia, name='listado_energia'),
    path('particula/', views.listado_particulas, name='listado_particula'),
    path('energia/nueva/', views.crear_energia, name='crear_energia'),
    path('particula/nueva/', views.crear_particula, name='crear_particula'),
]
