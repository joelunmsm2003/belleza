
from django.conf.urls import patterns, include, url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from app.views import *

from django.contrib import admin


admin.site.site_header = 'Capital'

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', 'jwt_auth.views.obtain_jwt_token'),
    url(r'api-token-refresh/', refresh_jwt_token),
    url(r'^', admin.site.urls),
    url(r'^agente/$', Agenterest.as_view()),
    url(r'^userfono/$', Userfono.as_view()),
    url(r'^creacliente/$', Creacliente.as_view()),
    url(r'^creapropuesta/$', Creapropuesta.as_view()),
    url(r'^listaramos/$', Listaramos.as_view()),
    url(r'^listacia/(\d+)$', Listacia.as_view()),
    url(r'^listaproducto/(\d+)/(\d+)$', Listaproducto.as_view()),
    url(r'^listapropuestas/(\d+)$', Listapropuestas.as_view()),
    url(r'^cliente/(\d+)$', Listacliente.as_view()),
    url(r'^clientes/$', TodosClientes.as_view()),
    url(r'^detallepropuesta/(\d+)$', Detallepropuesta.as_view()),
    url(r'^creacita/$', Creacita.as_view()),
    url(r'^citasagente/$', Citasagente.as_view()),
    url(r'^iconos/$', IconosLista.as_view()),
    url(r'^termometro/$', Termometro.as_view()),
    url(r'^metricas/(\d+)/(\d+)/(\d+)/(\d+)$', Metricas.as_view()),
    url(r'^modalidad/$', ListaModalidad.as_view()),
    url(r'^pariente/$', CreaPariente.as_view()),
    url(r'^gestion/$', MiGestion.as_view()),
    url(r'^updatecita/$', Updatecita.as_view()),
    url(r'^resumen/$', Resumen.as_view()),
    url(r'^creapos/$', Creapos.as_view()),
    url(r'^semanas/$', Semanasall.as_view()),
    url(r'^calculo/(\d+)$', Calculo.as_view()),
    url(r'^calculomes/$', Calculomes.as_view()),
    url(r'^losarchivos/$', Losarchivos.as_view()),
    url(r'^uploadphoto/', Uploadphoto.as_view()),
    url(r'^eliminapropuesta/(\d+)', Eliminarpropuesta.as_view()),
    url(r'^eliminarcita/(\d+)', Eliminarcita.as_view()),
]
