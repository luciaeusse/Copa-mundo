from django.db import models

# Create your models here.

class Continente(models.Model):
    nombreContinente = models.CharField(max_length=50)
    def __unicode__(self):
        return unicode(self.nombreContinente)


class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente)
    tecnico = models.CharField(max_length=60)
    def __unicode__(self):
        return unicode(self.nombre)
 
class Jugador(models.Model):
    nombreJugador = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)
    equipo = models.CharField(max_length=50)
    estatura = models.CharField(max_length=50)
    pieHabil = models.CharField(max_length=50)
    tarjetaAmarilla = models.CharField(max_length=50)
    tarjetaRoja = models.CharField(max_length=50)
    lesionado = models.CharField(max_length=50)
    titular = models.CharField(max_length=50)
    goles = models.CharField(max_length=50)
    foto = models.CharField(max_length=50)
    def __unicode__(self):
        return unicode(self.nombreJugador)
