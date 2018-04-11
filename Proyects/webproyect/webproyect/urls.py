
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from webproyect import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    url(r'accounts/', include('accounts.urls')),
    
]
