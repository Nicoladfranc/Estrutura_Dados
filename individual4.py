class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def concatena(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    atual = l1
    while atual.prox is not None:
        atual = atual.prox

    atual.prox = l2  # Concatena as listas

    return l1  # Retorna a lista do resultado

l1 = Lista(1)
l1.prox = Lista(2)
l1.prox.prox = Lista(3)

l2 = Lista(4)
l2.prox = Lista(5)
l2.prox.prox = Lista(6)

lista_concatenada = concatena(l1, l2)
atual = lista_concatenada
while atual is not None:
    print(atual.info)
    atual = atual.prox
