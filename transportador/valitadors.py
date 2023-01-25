import re
from validate_docbr import CNPJ


def nome_invalido(nome):
    return nome.isdigit()
def cnpj_valido(numero_cnpj):
    cnpj = CNPJ()
    return cnpj.validate(numero_cnpj)

def latlong_valido(lat_long):
    match = re.match(r"^-?([1-8]?\d(\.\d+)?|90(\.0+)?),-?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$", lat_long)
    if match:
        return True
    else:
        return False
    
def endereco_valido(endereco):
    return len(endereco) == 2

def km_marco_zero_valido(km_marco_zero):
    return km_marco_zero.isnumeric()

