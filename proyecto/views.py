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
from .forms import EnergiaForm, ParticulaForm
from django.shortcuts import render, redirect
#crear energia formulario
def crear_energia(request):
    if request.method == "POST":
        form = EnergiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listado_energia")
    else:
        form = EnergiaForm()
    return render(request, "crear_energia.html", {"form": form})
#crear particula formulario
def crear_particula(request):
    if request.method == "POST":
        form = ParticulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listado_particula")
    else:
        form = ParticulaForm()
    return render(request, "crear_particula.html", {"form": form})