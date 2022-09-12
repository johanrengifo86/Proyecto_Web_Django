from django.shortcuts import render, HttpResponse

# Create your views here.
# Vistas del Proyecto web 

def home(request):
    return render(request, "Proyecto_WebApp/home.html")

def servicios(request):
    return render(request, "Proyecto_WebApp/servicios.html")

def tienda(request):
    return render(request, "Proyecto_WebApp/tienda.html")

def blog(request):
    return render(request, "Proyecto_WebApp/blog.html")

def contacto(request):
    return render(request, "Proyecto_WebApp/contacto.html")
