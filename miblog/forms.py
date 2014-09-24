from django import forms


class FormComentario(forms.Form):
    comentario_texto = forms.CharField(label="comentario", max_length=200)
