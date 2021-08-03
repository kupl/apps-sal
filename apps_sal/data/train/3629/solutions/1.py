def array_mash(a, b):
    lista = []
    c = len(a)
    for i in range(len(a)):
        lista.append(a[i])
        lista.append(b[i])
    return lista
