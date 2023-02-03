from django.contrib import admin
from .models import *


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cpf', 'data_nascimento', 'data_cadastro')
    list_display_links = ('nome', 'telefone', 'cpf')
    search_fields = ('nome', 'telefone', 'cpf')
    list_per_page = 10


admin.site.register(Cliente, ClienteAdmin)


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'placa', 'cor', 'ano', 'cliente')
    list_display_links = ('marca', 'modelo', 'ano')
    search_fields = ('marca', 'modelo', 'ano')
    list_per_page = 10


admin.site.register(Veiculo, VeiculoAdmin)
