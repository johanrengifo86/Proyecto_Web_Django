from django.urls import path
from .views import VRegistro #Importación views


urlpatterns = [
   
    # Urls para cada View

    path('', VRegistro.as_view(), name="Autenticacion"),
]