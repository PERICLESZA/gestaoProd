from django.forms import ModelForm
from .models import Produto


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'valor', 'data', 'hora', 'imagem']
