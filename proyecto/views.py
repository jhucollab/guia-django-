from django.shortcuts import render
from .models import Energia, Particula
#listado energia
def listado_energia(request):
    energias = Energia.objects.all()
    return render(request, "listado_energia.html", {"energias": energias})
#listado particula
def listado_particulas(request):
    particulas = Particula.objects.all()
    return render(request, "listado_particula.html", {"particulas": particulas})

# Create your views here.
