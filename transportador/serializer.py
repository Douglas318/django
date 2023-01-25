from rest_framework import serializers
from transportador.models import Cadastro, MarcoZero, AreaDeCorte
from transportador.valitadors import *

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = '__all__'
    def validate(self, data):
        if nome_invalido(data['nome']):
            raise serializers.ValidationError({'nome':"O nome não deve possuir números"})
        if not cnpj_valido(data['cnpj']):
            raise serializers.ValidationError({'cnpj':"Você deve inserir um CNPJ válido"})      
        return data
        
class MarcoZeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcoZero
        fields = '__all__'
    def validate(self, data):
        if not endereco_valido(data['endereco']):
            raise serializers.ValidationError({'endereco':"Você deve inserir uma UF válida."})
        if not latlong_valido(data['lat_long']):
            raise serializers.ValidationError({'lat_long':"Você deve inserir uma latitude e longitude válida ex: -45.123456,-45.123456 "})
        return data
    
class AreaDeCorteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaDeCorte
        fields = '__all__'
        
class ListaAreaDeCorteCadastroSerializer(serializers.ModelSerializer):
    transportador = serializers.ReadOnlyField(source='transportador.nome')
    estado = serializers.ReadOnlyField(source='estado.endereco')
    class Meta:
        model = AreaDeCorte
        fields = ['transportador', 'km_marco_zero', 'estado']

    def validate(self, data):
        if not km_marco_zero_valido(data['km_marco_zero']):
            raise serializers.ValidationError({'km_marco_zero':"A distância do marco zero deve ser um número"})
        
        return data