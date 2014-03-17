from django.contrib import admin
from models import Equipo, Continente, Jugador
# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class ContinenteAdmin(admin.ModelAdmin):
    list_display = ('nombreContinente',)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombreJugador',)
 

admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Continente,ContinenteAdmin)
admin.site.register(Jugador,JugadorAdmin)
