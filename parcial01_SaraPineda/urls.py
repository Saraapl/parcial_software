from django.contrib import admin
from django.urls import path
from vuelos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('registrar/', views.registrar_vuelo, name="registrar_vuelo"),
    path('listar/', views.listar_vuelos, name="listar_vuelos"),
    path('estadisticas/', views.estadisticas, name="estadisticas"),
]
