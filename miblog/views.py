from django.shortcuts import render
from django.http import HttpResponse
from miblog.models import Entrada, Comentario
from miblog.forms import FormComentario
from django.utils import timezone
from django.contrib.auth.models import User

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
        comentario.entrada = Entrada.objects.get(pk=1)
        comentario.save()
        form = FormComentario(request.post)
        # if form.is_valid():
        #     print('Se guardó el comentario')
        #     form.save()
    else:
        print("entra qui")
        form = FormComentario
    return render(request, 'entradas.html', {'entradas': entradas , 'form': form})


def comentarios(request):
    if request.method == 'POST':
        comentario = Comentario()
        comentario.comentario_texto = request.POST['comentario_texto']
        comentario.comentario_fecha = timezone.now()
        comentario.usuario = 'wolvelopez'
        comentario.entrada = 1
        comentario.save()
        #form = FormComentario(request.post)
        # if form.is_valid():
        #     print('Se guardó el comentario')
        #     form.save()
    else:
        print("entra else")
        form = FormComentario()
    return render(request, 'prueba.html', {'form': form})    




