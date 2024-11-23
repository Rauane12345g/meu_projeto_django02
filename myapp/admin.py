from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')  # Exibir nome e preço na lista de produtos
    search_fields = ('nome',)  #buscar por nome

# Registra o modelo Produto com as configurações de admin
admin.site.register(Produto, ProdutoAdmin)

