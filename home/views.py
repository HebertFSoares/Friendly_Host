from django.shortcuts import render,redirect
from django.urls import reverse
from usuarios.models import Perfil
from django.contrib.auth.decorators import login_required

@login_required
def home_estudante(request):
    pefil = request.user.perfil
    if pefil.user_type == 'estudante':
        return render(request, 'home_estudante.html')
    else:
        return render(request, 'erro.html')

@login_required
def home_anfitriao(request):
    pefil = request.user.perfil
    if pefil.user_type == 'estudante':
        return render(request, 'home_anfitriao.html')
    else:
        return render(request, 'erro.html')