from django.shortcuts import render, redirect
from .models import Socios_Del_Club
from .forms import SociosForm
# Create your views here.

def index(request):
    return render(request, 'TEMPLATESAPP/index.html')

def Listado(request):
    Socios = Socios_Del_Club.objects.all()
    data = {'Socios' : Socios}
    return render(request, 'TEMPLATESAPP/Listado.html', data)

def agregar(request):
    form = SociosForm()
    data = {'form': form}

    if (request.method == 'POST'):
        form = SociosForm(request.POST)
        if (form.is_valid()):
            print("pruebavalid")
            form.save()
        else:
            
            return render(request, "TEMPLATESAPP/validarmalo.html")
        return index(request)
    
    data = {'form': form}
    return render(request, 'TEMPLATESAPP/agregar.html', data)

def Editar(request):
    return render(request, "TEMPLATESAPP/Editar.html")

def validarmalo(request):
    return render(request, "TEMPLATESAPP/validarmalo.html")

def eliminar_socio(request, id):
    socio = Socios_Del_Club.objects.get(id=id)
    socio.delete()
    return redirect("Listado")  


def editar_socio(request, id):
    socio = Socios_Del_Club.objects.get(id=id)

    if request.method == 'POST':
        form = SociosForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('Listado')  
    else:
        form = SociosForm(instance=socio)

    return render(request, 'TEMPLATESAPP/Editar.html', {'form': form})

def Usuario(request):
    return render(request, "TEMPLATESAPP/Usuario.html")