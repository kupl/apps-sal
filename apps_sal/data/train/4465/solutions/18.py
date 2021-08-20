def super_size(n):
    lista1 = list(str(n))
    lista = []
    for num in lista1:
        lista.append(num)
    for i in range(0, len(lista)):
        lista[i] = int(lista[i])
    lista.sort(reverse=True)
    lista_buna = int(''.join((str(i) for i in lista)))
    return lista_buna
