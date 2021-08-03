def even_numbers(arr, n):
    lista = []
    for i in arr[::-1]:
        if i % 2 == 0:
            lista.append(i)
            if len(lista) == n:
                return lista[::-1]
