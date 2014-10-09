from django.conf.urls import patterns, include, url
from miblog import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),    
    url(r'^$', views.mostrar_entradas, name='mostrar_entradas'),
    url(r'^(\d+)', views.entrada, name="entrada"),
)