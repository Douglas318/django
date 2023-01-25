from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=150, blank=False, null=False, unique=True)
    cnpj = models.CharField(max_length=18, blank=False, null=False, unique=True)

    def __str__(self):
        return self.nome
    
class MarcoZero(models.Model):
    endereco = models.CharField(max_length=150, blank=False, null=False, unique=True)
    lat_long = models.CharField(max_length=25, blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.endereco
    
class AreaDeCorte(models.Model):
    transportador = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    estado = models.ForeignKey(MarcoZero, on_delete=models.CASCADE)
    km_marco_zero = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return f"{self.transportador}, {self.estado}, {self.km_marco_zero}"
     
    
    