def max_number(n):
    n = str(n)
    lista = sorted(list(n), reverse=True)
    return int(''.join(lista))
