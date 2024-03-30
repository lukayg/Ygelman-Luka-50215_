from django.contrib import admin

# Register your models here.
from .models import *

class JuegoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cantidad")

class ConsolaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cantidad")

admin.site.register(Juego, JuegoAdmin)
admin.site.register(Consola, ConsolaAdmin)
admin.site.register(Todos_los_productos)
admin.site.register(Quienes_somos)
admin.site.register(Argames)