from django.http import response
from rest_framework.test import APITestCase
from transportador.models import Cadastro
from django.urls import reverse
from rest_framework import status


class CadastrosTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Cadastros-list')
        self.cadastro_1 = Cadastro.objects.create(
            nome='Transportador_teste_1', cnpj='85197738000143'
        )
        self.cadastro_2 = Cadastro.objects.create(
            nome='Transportador_teste_2', cnpj='78763997000129'
        )
        
    
    def test_requisicao_get_listar_transportadores(self):
        """Teste para verificar se a requisição GET está funciionando corretamente"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_cadastrar_transportador(self):
        """Teste para verificar se a requisição POST está funciionando corretamente"""
        data = {
            'nome':'Transportador_teste_3',
            'cnpj': '42614751000148'
        }
        
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        
    def test_requisicao_delete_cadastro_transportador(self):
        """Teste para verificar se a requisição DELETE está funciionando corretamente"""
        response = self.client.delete('/cadastros/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_requisicao_put_cadastro_transportador(self):
        """Teste para verificar se a requisição PUT está funciionando corretamente"""
        data = {
            'nome': 'Novo transportador_teste_3',
            'cnpj': '75841543000130'
        }
        
        response = self.client.put('/cadastros/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)