from django.shortcuts import render
from .models import Energia
#listado energia
def listado_energia(request):
    Energia = Energia.objects.all()
    return render(request, "listado_enegia.html", {"energias:", Energia})
#listado particula
def listado_particulas(request):
    Particula = Particula.objects.all()
    return render(request, "listado_particula.html", {"particulas:", Particula})

# Create your views here.
