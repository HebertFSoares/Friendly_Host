from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Perfil
from django.http import HttpResponse
import time

def cadastro(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirma_senha = request.POST.get("confirma_senha")
        data_nascimento = request.POST.get("data_nascimento")
        user_type = request.POST.get("user_type")
        estado_civil = request.POST.get("estado_civil")
        cpf_estudante = request.POST.get("cpf")
        cpf_anfitriao = request.POST.get("cpf_anfitriao")
        telefone = request.POST.get("telefone")
        nome_pai = request.POST.get("nome_pai")
        nome_mae = request.POST.get("nome_mae")
        instituicao = request.POST.get("instituicao")
        periodo = request.POST.get("periodo")
        resumo_academico = request.POST.get("resumo_academico")
        endereco = request.POST.get("endereco")
        descricao_espaco = request.POST.get("descricao_espaco")
        comodidades = request.POST.get("comodidades")
        
        # Verificações
        if not (senha == confirma_senha):
            return redirect(reverse('cadastro'))
        
        # Cria um novo usuário
        
        username = f"{usuario}_{int(time.time())}"
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
         # Cria o perfil do usuário com os campos extras
         
        perfil = Perfil.objects.create(
            usuario = user,
            data_nascimento = data_nascimento,
            user_type = user_type,
            estado_civil = estado_civil,
            cpf_estudante = cpf_estudante,
            telefone_estudante = telefone,
            nome_pai = nome_pai,
            nome_mae = nome_mae,
            instituicao = instituicao,
            periodo = periodo,
            resumo_academico = resumo_academico,
            cpf_anfitriao = cpf_anfitriao,
            telefone_anfitriao = telefone,
            endereco = endereco,
            descricao_espaco = descricao_espaco,
            comodidades = comodidades
         )
        
        return render(HttpResponse("Certo"))
    
    elif request.method == "GET":
        return render(request, 'cadastro.html')