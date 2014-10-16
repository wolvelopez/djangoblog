from django.contrib import admin
from miblog.models import Entrada, Comentario
from django_summernote.admin import SummernoteModelAdmin

class EntradaAdmin(SummernoteModelAdmin):
 	pass

admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Comentario)

