from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Vecino


# Create your views here.
def index(request):
    return render(request, "yo_alcalde/base.html")


def login(request):
    message = request.GET.get("message", None)
    return render(request, "yo_alcalde/login.html", {"message": message})


def registro(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        a_paterno = request.POST["paterno"]
        a_materno = request.POST["materno"]
        fecha_nacimiento = request.POST["fecha_nacimiento"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]

        rut_db = Vecino.objects.filter(rut=rut).exists()
        if not rut_db:
            Vecino.objects.create(
                rut=rut, nombre=nombre, apaterno=a_paterno, amaterno=a_materno,
                nacimiento=fecha_nacimiento, genero=genero, telefono=telefono, correo=correo
            )
            return HttpResponseRedirect(reverse("login") + "?message=" + f"{nombre} {a_paterno} {a_materno} se ha registrado exitosamente")

        else:
            return render(
                request,
                "yo_alcalde/registro.html",
                {"message": "El RUT ya ha sido utilizado en el sistema."},
            )
    else:
        return render(request, "yo_alcalde/registro.html")
