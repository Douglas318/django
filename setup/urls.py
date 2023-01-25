
from django.contrib import admin
from django.urls import path, include
from transportador.views import CadastrosViewSet, MarcoZeroViewSet, AreaDeCorteViewSet, ListaAreaDeCorteCadastro
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cadastros', CadastrosViewSet, basename='Cadastros')
router.register('marcozero', MarcoZeroViewSet, basename='Marco_zero')
router.register('area-de-corte', AreaDeCorteViewSet, basename='Areas_de_corte')

urlpatterns = [

    path('controle/', admin.site.urls),
    path('', include(router.urls)),
    path('cadastros/<int:pk>/area-de-corte/', ListaAreaDeCorteCadastro.as_view())   
]
