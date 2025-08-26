from django.shortcuts import render, redirect
from .models import Flight
from django.db.models import Avg


def home(request):
    return render(request, "home.html")


def registrar_vuelo(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        tipo = request.POST.get("tipo")
        precio = request.POST.get("precio")

        if nombre and tipo and precio:
            Flight.objects.create(
                nombre=nombre,
                tipo=tipo,
                precio=precio
            )
            return redirect("listar_vuelos")
    return render(request, "registrar.html")


def listar_vuelos(request):
    vuelos = Flight.objects.all().order_by("precio")
    return render(request, "listar.html", {"vuelos": vuelos})


def estadisticas(request):
    total_nacionales = Flight.objects.filter(tipo="Nacional").count()
    total_internacionales = Flight.objects.filter(tipo="Internacional").count()
    promedio_nacional = Flight.objects.filter(tipo="Nacional").aggregate(promedio=Avg("precio"))["promedio"]

    return render(request, "estadisticas.html"), {
        "total_nacionales": total_nacionales,
        "total_internacionales": total_internacionales,
        "promedio_nacional": promedio_nacional

    }