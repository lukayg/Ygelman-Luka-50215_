from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    #___________________________Menu Principal___________________________
    path('', home, name="home"),
    path('juegos/', juegos, name="juegos"),
    path('consolas/', consolas, name="consolas"),
    path('todos_los_productos/', todos_los_productos, name="todos_los_productos"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),

    #____________________________Otras paginas___________________________
    path('acerca_de_mi/', acerca_de_mi, name="acerca_de_mi"),

    #____________________________Formularios_____________________________

    path('juegosForm/', juegoForm, name="juegosform"),
    path('consolasform/', consolasForm, name="consolasform"),


]