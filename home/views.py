from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Perfil

@login_required
def home_estudante(request):
        return render(request, 'home_estudante.html')

@login_required
def home_anfitriao(request):
    return render(request, 'home_estudante.html')