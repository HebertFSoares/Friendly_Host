from django import forms

class AdicionarVagaForm(forms.Form):
    titulo = forms.CharField(label='Título da Casa', max_length=100)
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea)
    localizacao = forms.CharField(label='Localização', max_length=200)
    capacidade = forms.IntegerField(label='Capacidade de Acomodação')
    regras_casa = forms.CharField(label='Regras da Casa', widget=forms.Textarea)
    informacoes_familia = forms.CharField(label='Informações sobre a Família', required=False, widget=forms.Textarea)
    contato = forms.CharField(label='Contato', max_length=100)
