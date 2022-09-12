from django.urls import path

from Proyecto_WebApp import views #Importación views

urlpatterns = [
   
    # Urls para cada View
    path('', views.home, name="Home"),
    path('servicios/', views.servicios, name="Servicios"),
    path('tienda/', views.tienda, name="Tienda"),
    path('blog/', views.blog, name="Blog"),
    path('contacto/', views.contacto,name="Contacto"),
]