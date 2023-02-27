from django.shortcuts import render

def contactos_inicio(request):
    return render(request, "contactos/inicio.html", {})

