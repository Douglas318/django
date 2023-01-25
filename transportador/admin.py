from django.contrib import admin

from transportador.models import Cadastro, MarcoZero, AreaDeCorte

class Cadastros(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cnpj',)
    list_per_page = 10
    
admin.site.register(Cadastro, Cadastros)

class MarcosZero(admin.ModelAdmin):
    list_display = ('id', 'endereco', 'lat_long')
    list_display_links = ('id', 'endereco')
    search_fields = ('endereco', 'lat_long',)
    list_per_page = 10
    
admin.site.register(MarcoZero, MarcosZero)

class AreasDeCorte(admin.ModelAdmin):
    list_display = ('id', 'km_marco_zero')
    list_display_links = ('id',)
    list_per_page = 10
    ordering = ('id', )
admin.site.register(AreaDeCorte, AreasDeCorte)