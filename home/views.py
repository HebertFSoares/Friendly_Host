from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Perfil
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import AdicionarVagaForm
from .models import VagaCasa
from django.contrib import messages
from django.contrib.messages import constants
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy

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
    if not is_estudante(request.user) and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('error'))
    return render(request, 'home_estudante.html')

@login_required
def home_anfitriao(request):
    if not is_estudante(request.user) and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('error'))
    return render(request, 'home_anfitriao.html')

def error(request):
    return render(request, 'erro.html')

class AdicionarVagaView(CreateView):
    model = 'VagaCasa'
    form_class = AdicionarVagaForm
    template_name = 'adicionar_vaga.html'
    success_url = reverse_lazy('adicionar_vaga')
    
    def form_valid(self, form):
        messages.success(self.request, 'Vaga adicionada com sucesso!')
        return super().form_valid(form)
    
class VagasListView(ListView):
    model = VagaCasa
    template_name = 'list_vaga.html'
    context_object_name = 'vagas'