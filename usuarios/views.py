from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirma_senha = request.POST.get("confirma_senha")
        
        if not (senha == confirma_senha):
            return redirect(reverse('cadastro'))
        
        #TODO: adicionar mais verificações!
        