from rest_framework import serializers
from .models import Cliente, Veiculo


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
    nome_cliente = serializers.CharField(source='cliente.nome', read_only=True)

    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'placa', 'cor', 'ano', 'nome_cliente']


class ListaVeiculosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'placa']
