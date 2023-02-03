from rest_framework import viewsets, generics, filters
from .serializer import *


class ClienteViewSet(viewsets.ModelViewSet):
    """Lista todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome']
    ordering_fields = ['nome']


class VeiculoViewSet(viewsets.ModelViewSet):
    """Lista todos os veículos"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class ListaVeiculosCliente(generics.ListAPIView):
    """Lista todos os veículos de um cliente"""

    def get_queryset(self):
        queryset = Veiculo.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaVeiculosClienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['modelo', 'placa']
