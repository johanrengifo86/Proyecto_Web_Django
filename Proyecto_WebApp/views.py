from django.shortcuts import render, HttpResponse


# Create your views here.
# Vistas del Proyecto web 

def home(request):
    return render(request, "Proyecto_WebApp/home.html")


def tienda(request):
    return render(request, "Proyecto_WebApp/tienda.html")


