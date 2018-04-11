from django.conf.urls import url, include
from crud_jugadores.views import JugadorCreate,JugadorList, JugadorDelete, JugadorUdate,JugadorShow
from . import views
app_name="crud_jugaodores"
urlpatterns = [
   
    url(r'^nuevo/', JugadorCreate.as_view(), name='jugador_crear'),
    url(r'^list/', JugadorList.as_view(), name='jugador_listar'),
    url(r'^update/(?P<pk>\d+)/$', JugadorUdate.as_view(), name='jugador_update'),
    url(r'^delete/(?P<pk>\d+)/$', JugadorDelete.as_view(), name='jugador_delete'),
     url(r'^show/(?P<pk>\d+)/$', JugadorShow.as_view(), name='jugador_show'),
     url(r'^search/$', views.search, name='jugador_search'),
]