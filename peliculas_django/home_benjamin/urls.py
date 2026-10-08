from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('accion/', views.accion, name='accion'),
    path('terror/', views.terror, name='terror'),
]