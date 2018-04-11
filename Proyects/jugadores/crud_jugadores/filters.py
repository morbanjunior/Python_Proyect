import django_filters
from crud_jugadores.models import Jugador

class JugadorFilter(django_filters.FilterSet):
    class Meta:
        model = Jugador
        fields = ['id', 'nombres','email', 'apellidos']