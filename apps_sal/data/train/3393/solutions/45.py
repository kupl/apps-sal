import functools
def list_squared(m, n):
    lista_final = []
    lst = []
    for i in range(m,n):
        dic = factors(i)
        for el in dic:
            lst.append(el**2)   
        soma = sum(lst)
        numero = soma ** (0.5)
        if numero == int(numero):
            lista_final = lista_final + [[i, soma]]
        lst = []
    return lista_final

def factors(n):    
    return set(functools.reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
            

