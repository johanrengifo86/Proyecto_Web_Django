from django.urls import path
from .views import VRegistro, cerrar_sesion #Importación views


urlpatterns = [
   
    # Urls para cada View

    path('', VRegistro.as_view(), name="Autenticacion"),

    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
]