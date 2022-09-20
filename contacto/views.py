from django.shortcuts import render, redirect
from . forms import FormularioContacto 

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()

# Procedimiento para rescatar la informacion del formulario
    if request.method == "POST": # si el metodo de la peticion es igual Post
        formulario_contacto = FormularioContacto(data=request.POST) # carga la informacion del formulario en el constructor
        if formulario_contacto.is_valid(): # si la informacion es valida
            # Guarda en las variables la informacion 
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
        # Redirecciona a la pagina de contacto despues del envio de datos
            return redirect("/contacto/?valido")

    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
