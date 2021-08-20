def remove_char(s):
    lista = list(s)
    del lista[0]
    del lista[-1]
    s = ''.join(lista)
    return s
