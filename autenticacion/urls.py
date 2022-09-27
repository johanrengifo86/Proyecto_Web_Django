from django.urls import path

from . import views #Importación views


urlpatterns = [
   
    # Urls para cada View

    path('', views.autenticacion,name="Autenticacion"),
]