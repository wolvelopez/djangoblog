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
        comentario = Comentario()
        comentario.comentario_texto = request.POST['comentario_texto']
        comentario.comentario_fecha = timezone.now()
        comentario.usuario = User.objects.get(username='wolvelopez')
        comentario.entrada = Entrada.objects.get(pk=request.POST['id'])
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
    if request.user.is_authenticated:
        usuario = 1
    else:
        usuario = 0
    return render(request, 'entradas.html', 
        {'entradas': entradas , 'usuario': usuario})

def entrada(entrada_id):
    entradaSel = Entrada.object.get(pk=entrada_id)
    return render(request, 'entrada.html', {'entradasel':entradaSel})

def logout_view(request):
    logout(request)
    print("llega acá????")
    return HttpResponseRedirect('/entradas/')    
