from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from crud_jugadores.models import Jugador 
from crud_jugadores.forms import JugadoresForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from crud_jugadores.filters import JugadorFilter

class JugadorCreate(CreateView):
    model = Jugador
    form_class = JugadoresForm
    template_name = 'crudjugadores/jugador_form.html'
    success_url = reverse_lazy('jugadores:jugador_listar')


class JugadorList(ListView):
    queryset = Jugador.objects.order_by('id')
    template_name= 'crudjugadores/jugador_list.html'
    paginate_by = 5

class JugadorUdate(UpdateView):
    model = Jugador
    form_class = JugadoresForm
    template_name = 'crudjugadores/jugador_form.html'
    success_url = reverse_lazy('jugadores:jugador_listar')

class JugadorDelete(DeleteView):
    model = Jugador
    form_class = JugadoresForm
    template_name = 'crudjugadores/jugador_delete.html'
    success_url = reverse_lazy('jugadores:jugador_listar')

class JugadorShow(DetailView):
    model = Jugador
    form_class = JugadoresForm
    template_name = 'crudjugadores/jugador_show.html'
   
def search(request):
    jugador_list = Jugador.objects.all()
    jugador_filter = JugadorFilter(request.GET,queryset = jugador_list)

    return render(request, 'crudjugadores/jugador_list2.html',{'filter':jugador_filter})




