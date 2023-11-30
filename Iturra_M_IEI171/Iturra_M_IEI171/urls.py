"""
URL configuration for Iturra_M_IEI171 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("Listado/", views.Listado, name="Listado"),
    path("agregar/", views.agregar, name="agregar" ),
    path("Editar/", views.Editar, name="Editar"),
    path("validarmalo/", views.validarmalo, name="validarmalo"),
    path('eliminar/<int:id>/', views.eliminar_socio, name='eliminar_socio'),
    path('editar/<int:id>/', views.editar_socio, name='editar_socio'),
    path("Usuario/", views.Usuario, name="Usuario"),
]
