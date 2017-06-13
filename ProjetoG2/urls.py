from django.conf.urls import url, include
from tastypie.api import Api
from django.contrib import admin
from avalia.api.resources import UsuarioResource, EventoResource, ArtigoResource, AvaliacaoResource


v1_api = Api(api_name='v1')
v1_api.register(UsuarioResource())
v1_api.register(EventoResource())
v1_api.register(ArtigoResource())
v1_api.register(AvaliacaoResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
]
