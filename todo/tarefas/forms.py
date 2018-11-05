from django import forms

from .models import Categoria, Tarefa

class CategoriaForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Categoria
        fields = '__all__' #mostra todos os campos
        # fields = ('nome','descricao') Para escolhe os campos que vc quer mostrar
        # exclude = ('nome','descricao',) Para escolher os campos que vc NÃO que mostrar

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__' 


