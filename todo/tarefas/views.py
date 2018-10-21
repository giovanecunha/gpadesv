from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .forms import CategoriaForm, TarefaForm

def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HTTPResponse('Categoria adicionada com sucesso!')
        else:
            print(forms.erros)
    else:
        form = CategoriaForm()
    return render(request, 'tarefas/nova_categoria.html', {'form':form}) 

def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return HTTPResponse('Tarefa adicionada com sucesso!')
        else:
            print(forms.erros)
    else:
        form = TarefaForm()
    return render(request, 'tarefas/nova_tarefa.html', {'form':form}) 
