def distinct(seq):
    lista_filtrada = []
    for i in seq:
        if i not in lista_filtrada:
            lista_filtrada.append(i)
    return(lista_filtrada)
