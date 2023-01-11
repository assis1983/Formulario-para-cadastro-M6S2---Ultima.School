from django import forms


class ContatoForm(forms.Form):
    nome_do_Pet = forms.CharField()
    telefone_do_responsável = forms.CharField()
    data_da_reserva = forms.DateField()
    mensagem = forms.CharField(widget=forms.Textarea)
