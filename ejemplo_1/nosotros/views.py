from django.shortcuts import render

def nosotros_inicio(request):
    return render(request, "nosotros/inicio.html", {})


def nosotros_nuestro_equipo(request):
    return render(request, "nosotros/nuestro_equipo.html", {})

def nosotros_nuestro_equipo_detalle(request, id, slug):
    nombre = "Andres Valencia"
    estaciones = ["verano", "primavera", "otoño","invierno"]
    return render(request, "nosotros/nuestro_equipo_detalle.html", {'id': id, 'slug': slug, 'nombre': nombre, 'estaciones': estaciones})
