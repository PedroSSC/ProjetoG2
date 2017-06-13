from tastypie.resources import ModelResource
from tastypie import fields
from avalia.models import Evento, Artigo, Avaliacao
from django.contrib.auth.models import User
from tastypie.exceptions import NotFound
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
from tastypie.exceptions import Unauthorized

#-----------------RESOURCE USUARIO-------------------------#
class UsuarioResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get','post', 'delete','put']
        aways_return_data = True
        authentication = ApiKeyAuthentication()
        filtering = {
            "Name": ('exact', 'startswith',)
        }

    def obj_create(self, bundle, **kwargs):
        print(bundle)
        if not(User.objects.filter(username = bundle.data['username'])):
            user = User()
            user.username = bundle.data['username']
            user.email = bundle.data['email']
            user.password = bundle.data['password']
            user.save()
            bundle.obj = user
            return bundle
        else:
            raise Unauthorized('Já existe Usuário com esse nome.')

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Não permitido.')



#-----------------RESOURCE EVENTO-------------------------#
class EventoResource(ModelResource):
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get','post', 'delete','put']
        aways_return_data = True
        authentication = ApiKeyAuthentication()
        filtering = {
            "nome": ('exact', 'startswith',)
        }

    def obj_create(self, bundle, **kwargs):
        usuario = bundle.request.user
        nome = bundle.data['nome']
        evento = Evento()
        evento.administrador = User.objects.get(pk=usuario.pk)
        evento.nome = nome
        evento.save()
        bundle.objeto = evento

    def obj_update(self, bundle, **kwargs):
        evento = Evento.objects.get(pk=kwargs['pk'])
        admEvento = User.objects.get(username=tarefa.usuario)
        solicitante = bundle.request.user
        if(admEvento.pk == solicitante.pk):
            nome = bundle.data['nome']
            tarefa.nome = bundle.data['nome']
            tarefa.administrador = User.objects.get(pk = usuario[4])
            tarefa.save()
            bundle.obj = tarefa
            return bundle
        else:
            raise Unauthorized('Apenas o Administrador deste evento pode alterá-lo.')


    def obj_delete(self, bundle, **kwargs):
        evento = Evento.objects.get(pk=kwargs['pk'])
        admEvento = User.objects.get(username=evento.administrador)
        solicitante = bundle.request.user
        if(admEvento.pk == solicitante.pk):
            ArtigoEvento = Artigo.objects.filter(evento = evento)
            if(ArtigoEvento.__len__() == 0):
                evento.delete()
                bundle.obj = artigo
            else:
                raise Unauthorized('Existem artigos cadastrado neste Evento.')
        else:
            raise Unauthorized('Apenas o Administrador pode excluir este Evento.')

        def obj_delete_list(self, bundle, **kwargs):
            raise Unauthorized('Não permitido.')


#-----------------RESOURCE ARTIGO-------------------------#
class ArtigoResource(ModelResource):
    class Meta:
        queryset = Artigo.objects.all()
        allowed_methods = ['get','post', 'delete','put']
        aways_return_data = True
        authentication = ApiKeyAuthentication()
        filtering = {
            "nome": ('exact', 'startswith',)
        }

    def obj_create(self, bundle, **kwargs):
        autor = bundle.request.user
        print(autor)
        nome = bundle.data['nome']
        evento = bundle.data['evento'].split("/")
        artigo = Artigo()
        artigo.autor = User.objects.get(pk=autor.pk)
        artigo.nome = nome
        artigo.evento = Evento.objects.get(pk=evento[4])
        artigo.save()
        bundle.obj = artigo
        return bundle

    def obj_get_list(self, bundle, **kwargs):
        solicitante = bundle.request.user
        return Artigo.objects.filter(autor = solicitante)


    def obj_delete(self, bundle, **kwargs):
        artigo = Artigo.objects.get(pk=kwargs['pk'])
        autorArtigo = User.objects.get(username=artigo.autor)
        solicitante = bundle.request.user
        if(autorArtigo.pk == solicitante.pk):
            print(artigo)
            AvaliaArtigo = Avaliacao.objects.filter(artigo = artigo)
            if(AvaliaArtigo.__len__() == 0):
                artigo.delete()
                bundle.obj = artigo
            else:
                raise Unauthorized('Existem artigos cadastrado neste Evento.')
        else:
            raise Unauthorized('Apenas o Administrador pode excluir este Evento.')


    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Não permitido.')


#-----------------RESOURCE AVALIACAO-------------------------#
class AvaliacaoResource(ModelResource):
    class Meta:
        queryset = Avaliacao.objects.all()
        allowed_methods = ['get','post', 'delete','put']
        aways_return_data = True
        authentication = ApiKeyAuthentication()
        filtering = {
            "nome": ('exact', 'startswith',)
        }

    def obj_create(self, bundle, **kwargs):
            avaliador = bundle.request.user
            artigo = bundle.data['artigo'].split("/")
            qualidade = bundle.data['qualidade']
            inovacao = bundle.data['qualidade']
            resultados = bundle.data['qualidade']
            metodologia = bundle.data['qualidade']
            adequacao = bundle.data['qualidade']
            contAval = Avaliacao.objects.filter(artigo = artigo[4], avaliador = avaliador)
            if(contAval.__len__() == 0):
                avaliacao = Avaliacao()
                avaliacao.avaliador = User.objects.get(pk=avaliador.pk)
                avaliacao.artigo = Artigo.objects.get(pk=artigo[4])
                avaliacao.save()
                bundle.obj = avaliacao
                return bundle
            else:
                raise Unauthorized('Avaliação já realizada.')

    def obj_delete(self, bundle, **kwargs):
        avaliacao = Avaliacao.objects.get(pk=kwargs['pk'])
        autorAvalia = User.objects.get(username=avaliacao.avaliador)
        solicitante = bundle.request.user
        if(autorAvalia.pk == solicitante.pk):
            artigo.delete()
            bundle.obj = artigo
        else:
            raise Unauthorized('Apenas o Avaliadior pode excluir esta Avaliação.')

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Não permitido.')
