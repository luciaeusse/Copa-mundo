from django.contrib import admin
from models import Equipos, Continente
# Register your models here.


class EquiposAdmin(admin.ModelAdmin):
    list_display=('nombre',)


class ContinenteAdmin(admin.ModelAdmin):
    list_display=('nombreContinente',)

admin.site.register(Equipos,EquipoAdmin)

