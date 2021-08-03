def merge_arrays(arr1, arr2):
    lista = []
    a = sorted(arr1) + sorted(arr2)
    a.sort()
    for i in a:
        if i not in lista:
            lista.append(i)
    return lista
