from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from usuarios.models import Perfil
from django.urls import reverse
from django.http import HttpResponseRedirect

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
def home_estudante(request):
    if not is_estudante(request.user):
        return HttpResponseRedirect(reverse('error'))
    return render(request, 'home_estudante.html')

@login_required
def home_anfitriao(request):
    if not is_anfitriao(request.user):
        return HttpResponseRedirect(reverse('error'))
    return render(request, 'home_anfitriao.html')

def error(request):
    return render(request, 'erro.html')