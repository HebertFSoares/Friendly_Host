from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from usuarios.models import Perfil

def is_estudante(user):
    try:
        perfil = Perfil.objects.get(usuario=user)
        return perfil.user_type == 'estudante'
    except Perfil.DoesNotExist:
        return False

def is_anfitriao(user):
    try:
        perfil = Perfil.objects.get(usuario=user)
        return perfil.user_type == 'anfitriao'
    except Perfil.DoesNotExist:
        return False

@login_required
@user_passes_test(is_estudante)
def home_estudante(request):
    return render(request, 'home_estudante.html')

@login_required
@user_passes_test(is_anfitriao)
def home_anfitriao(request):
    return render(request, 'home_anfitriao.html')
