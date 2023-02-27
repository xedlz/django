from django.shortcuts import render
from django.http import HttpResponse, Http404


def diseno_inicio(request):
    #return HttpResponse("hola mundo con las manos en el código")
    return render(request, "diseno/home.html", {})



