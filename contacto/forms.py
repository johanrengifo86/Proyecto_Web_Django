from distutils.command.config import LANG_EXT
import email
from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label ="Email", required=True)
    contenido = forms.CharField(label="Contenido")
