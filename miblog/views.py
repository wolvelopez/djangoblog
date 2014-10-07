from django.shortcuts import render
from django.http import HttpResponse
from miblog.models import Entrada, Comentario
from miblog.forms import FormComentario
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponse('Bienvenido al blog :)')


#@login_required
def mostrar_entradas(request):
    entradas = Entrada.objects.all()    
    if request.method == 'POST':
        entrada_pk = request.POST['comentario_texto.id']
        print("Entrada_PK: %s" % entrada_pk)
        comentario = Comentario()
        comentario.comentario_texto = request.POST['comentario_texto']
        comentario.comentario_fecha = timezone.now()
        comentario.usuario = User.objects.get(username='wolvelopez')
        comentario.entrada = Entrada.objects.get(pk=1)
        comentario.save()
        #obtencion del usuario autenticado
        if request.user.is_authenticated():
            usuario = User
        else:
            return HttpResponseRedirect('/accounts/login/')
    else:
        print("entra qui")
        #form = FormComentario
        usuario = None
    return render(request, 'entradas.html', 
        {'entradas': entradas , 'usuario': usuario})

def logout_view(request):
    logout(request)
    print("llega acá????")
    return HttpResponseRedirect('/entradas/')    
