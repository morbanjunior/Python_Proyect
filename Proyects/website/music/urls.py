from django.conf.urls import url
from . import views
#Index conf.

app_name='music'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),  name='index'),
    url(r'^register/$',views.UserFormView.as_view(),  name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),  name='detail'),
   
   #/music/album/add/
   url(r'album/add/$', views.AlbumCreate.as_view(),  name='album-add'),

   #/music/album/pk/
   url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(),  name='album-Update'),

   #/music/album/pk/delete
   url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(),  name='album-delete'),
    
]