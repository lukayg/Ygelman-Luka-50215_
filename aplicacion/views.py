from django.shortcuts import render

from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def juegos(request):
    contexto = {'juegos': Juego.objects.all()}
    return render(request, "aplicacion/juegos.html", contexto)

def consolas(request):
    contexto = {'consolas': Consola.objects.all()}
    return render(request, "aplicacion/consolas.html", contexto)

def todos_los_productos(request):
    return render(request, "aplicacion/todos_los_productos.html")

def quienes_somos(request):
    return render(request, "aplicacion/quienes_somos.html")

#_____________________________Otros____________________________
def acerca_de_mi(request):
    return render(request, "aplicacion/acerca_de_mi.html")


#_____________________________Forms____________________________
def juegoForm(request):
    if request.method == "POST":
        miForm = JuegosForm(request.POST)
        if miForm.is_valid():
            nombre_juego = miForm.cleaned_data.get("nombre")
            cantidad_juego = miForm.cleaned_data.get("cantidad")
            juego = Juego(nombre=nombre_juego, cantidad = cantidad_juego)
            juego.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = JuegosForm()

    return render(request, "aplicacion/juegosForm.html", {"forms": miForm})

def consolasForm(request):
    if request.method == "POST":
        miForm = ConsolaForm(request.POST)
        if miForm.is_valid():
            nombre_consola = miForm.cleaned_data.get("nombre")
            cantidad_consola = miForm.cleaned_data.get("cantidad")
            consola = Consola(nombre=nombre_consola, cantidad = cantidad_consola)
            consola.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = ConsolaForm()

    return render(request, "aplicacion/consolasForm.html", {"forms": miForm})