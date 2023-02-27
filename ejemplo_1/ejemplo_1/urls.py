from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name = "home_urls"),
    path('nosotros', include('nosotros.urls'), name="nosotros_urls"),
    path('contactos', include('contactos.urls'), name="contactos_urls"),
    path('diseno', include('diseno.urls'), name="diseno_urls"),

]
