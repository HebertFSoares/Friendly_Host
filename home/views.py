from django.shortcuts import render, redirect
from django.urls import reverse
from usuarios.models import Perfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def home_estudante(request):
    try:
        perfil = request.user.perfil
        if perfil.user_type == 'estudante':
            return render(request, 'home_estudante.html')
        else:
            return render(request, 'erro.html')  # Redirecionar para a página de acesso negado
    except Perfil.DoesNotExist:
        # Caso o perfil não exista, redirecionar para a página de acesso negado
        return render(request, 'erro.html')

@login_required
def home_anfitriao(request):
    try:
        perfil = request.user.perfil
        if perfil.user_type == 'anfitriao':
            return render(request, 'home_anfitriao.html')
        else:
           return render(request, 'erro.html')  # Redirecionar para a página de acesso negado
    except Perfil.DoesNotExist:
        # Caso o perfil não exista, redirecionar para a página de acesso negado
        return render(request, 'erro.html')
