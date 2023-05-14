from django.shortcuts import render, redirect
from django.urls import reverse
from usuarios.models import Perfil
from django.contrib.auth.decorators import login_required

@login_required
def home_estudante(request):
    try:
        perfil = request.user.perfil
        if perfil.user_type == 'estudante':
            return render(request, 'home_estudante.html')
        else:
            return render(request, 'erro.html')
    except Perfil.DoesNotExist:
        return render(request, 'erro.html')

@login_required
def home_anfitriao(request):
    try:
        perfil = request.user.perfil
        if perfil.user_type == 'anfitriao':
            return render(request, 'home_anfitriao.html')
        else:
           return render(request, 'erro.html')  
    except Perfil.DoesNotExist:
        return render(request, 'erro.html')
