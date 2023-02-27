from django.urls import path
from .views import *

urlpatterns = [
    path('', contactos_inicio, name="contactos_inicio"),

]
