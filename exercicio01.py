class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None
        

def cria_lista():
    return Lista()

def insere_lista(lst, valor):
    novo= Lista(valor)
    novo.prox = lst
    return novo

def lista_imprime(lst):
    atual= lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox
        
def lista_vazia(lst):
    return lst is None

def lista_busca(lst,valor):
    atual=lst
    while atual is not None:
        
        if atual.info==valor:
            return valor, "ta na lista"
        
        atual =atual.prox
    return valor, "Não ta na lista"

def lista_retira(lst, valor):
    if lst is None:
        return lst
    
    if lst.info == valor:
        return lst.prox

    atual = lst
    while atual.prox is not None:
        if atual.prox.info == valor:
            atual.prox = atual.prox.prox
            return lst
        atual = atual.prox

    return lst 
      
lst = cria_lista()
lst=insere_lista(lst, 50)
lst= insere_lista(lst, 60)
lst= insere_lista(lst, 70)
busca= lista_busca(lst,30)
lst= lista_retira(lst,50)

print(busca)

lista_imprime(lst)
