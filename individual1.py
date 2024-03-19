
class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def list_comprimento(lst):
    contador = 0
    atual = lst
    while atual is not None:
        contador += 1
        atual = atual.prox
    return contador

# Isto e uma lista encadeada ? tenho minhas duvidas...
lst = Lista(4)
lst.prox = Lista(2)
lst.prox.prox = Lista(5)
lst.prox.prox.prox = Lista(10)
lst.prox.prox.prox.prox = Lista(2)

comprimento = list_comprimento(lst)
print("Comprimento lista encadeada:",comprimento)
