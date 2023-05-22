from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('estudante/', views.home_estudante, name="home_estudante"),
    path('anfitriao/', views.home_anfitriao, name='anfitriao_home'),
    path('error/', views.error, name="error"),
    path('adicionar_vaga/', views.adicionar_vaga, name="adicionar_vaga"),
]
