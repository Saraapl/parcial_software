from django.shortcuts import render, redirect
from .models import Flight
from django.db.models import Avg


def home(request):
    return render(request, "vuelos/home.html")


def registrar_vuelo(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        tipo = request.POST.get("tipo")
        precio = request.POST.get("precio")

        if nombre and tipo and precio:
            Flight.objects.create(
                name=nombre,   
                type=tipo,     
                price=precio   
            )
            return redirect("listar_vuelos")
    return render(request, "vuelos/registrar.html")


def listar_vuelos(request):
    vuelos = Flight.objects.all().order_by("price")  
    return render(request, "vuelos/listar.html", {"vuelos": vuelos})


def estadisticas(request):
    total_nacionales = Flight.objects.filter(type="Nacional").count()
    total_internacionales = Flight.objects.filter(type="Internacional").count()
    promedio_nacional = Flight.objects.filter(type="Nacional").aggregate(promedio=Avg("price"))["promedio"]

    return render(request, "vuelos/estadisticas.html", {
        "total_nacionales": total_nacionales,
        "total_internacionales": total_internacionales,
        "promedio_nacional": promedio_nacional
    })
