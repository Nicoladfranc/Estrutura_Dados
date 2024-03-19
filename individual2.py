class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def maiores(lst, n):
    contador = 0
    atual = lst
    while atual is not None:
        if atual.info > n:
            contador += 1
        atual = atual.prox
    return contador

lst = Lista(5)
lst.prox = Lista(10)
lst.prox.prox = Lista(3)
lst.prox.prox.prox = Lista(8)

# parametro e para definir o valor de n
parametro = maiores(lst, 4)
print("Número de nós com valores maiores que 5:", parametro)
