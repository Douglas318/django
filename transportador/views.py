from rest_framework import viewsets, generics, filters
from transportador.models import Cadastro, MarcoZero, AreaDeCorte
from django_filters.rest_framework import DjangoFilterBackend

from transportador.serializer import (
    CadastroSerializer, 
    MarcoZeroSerializer, 
    AreaDeCorteSerializer, 
    ListaAreaDeCorteCadastroSerializer)

class CadastrosViewSet(viewsets.ModelViewSet):
    """exibindo todos os transportadores"""
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'cnpj']
    
class MarcoZeroViewSet(viewsets.ModelViewSet):
    """Exibindo todos os marco zeros"""
    queryset = MarcoZero.objects.all()
    serializer_class = MarcoZeroSerializer   
    
class AreaDeCorteViewSet(viewsets.ModelViewSet):
    """Exibindo todas as areas de corte"""
    queryset = AreaDeCorte.objects.all()
    serializer_class = AreaDeCorteSerializer
    
class ListaAreaDeCorteCadastro(generics.ListAPIView):
    """Exibe todas as areas de corte do transportador"""
    def get_queryset(self):
        queryset = AreaDeCorte.objects.filter(transportador=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAreaDeCorteCadastroSerializer
    
    