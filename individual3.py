class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

# Pelas minhas pesquisas referencia e os valores estranhos, mas na duvida coloquei para obter o valor tambem.
def ultimo(lst):
    if lst is None:
        return None, None

    atual = lst
    while atual.prox is not None:
        atual = atual.prox

    return atual, atual.info 

lst = Lista(5)
lst.prox = Lista(10)
lst.prox.prox = Lista(3)
lst.prox.prox.prox = Lista(8)

ultimo_no, ultimo_valor = ultimo(lst)
print("Referência do ultimo no:", ultimo_no)
print("Valor do ultimo no", ultimo_valor)
