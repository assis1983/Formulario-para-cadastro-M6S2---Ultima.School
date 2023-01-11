from django.shortcuts import render
from base.forms import ContatoForm

def cadastro(request):
    sucesso = False
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'telefone': '(18) 997974147',
        'responsavel' : 'Eder',
        'form':form,
        'sucesso':sucesso
    }
        
    
    return render(request, 'cadastrar.html', contexto)

