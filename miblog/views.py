from django.shortcuts import render
from django.http import HttpResponse
from miblog.models import Entrada, Comentario
from miblog.forms import FormComentario
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect

def index(request):    
        if request.user.is_authenticated():
            usuario = User            
        else:
            return HttpResponseRedirect('/accounts/login/')
        return render(request, 'index.html', {'usuario': usuario})

#@login_required
def mostrar_entradas(request):
    entradas = Entrada.objects.all()        
    return render(request, 'entradas.html', 
        {'entradas': entradas})


def entrada(request,entrada_id):
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
        usuario = None
    if request.user.is_authenticated:
        usuario = 1
    else:
        usuario = 0    
    
    entradaSel = Entrada.objects.get(id=entrada_id)
    comentarioSel = Comentario.objects.filter(entrada_id=entradaSel.id)
    print("entradaSel: %s" % entradaSel.id)
    print(comentarioSel)
    return render(request, 'entrada.html', 
        {'entradaSel': entradaSel , 'comentarioSel': comentarioSel})


def logout_view(request):
    logout(request)
    print("llega acá????")
    return HttpResponseRedirect('/entradas/')    
