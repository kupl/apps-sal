def max_number(n, vac=''):
    lista2 = [int(a) for a in list(str(n))]
    lista2.sort(reverse=True)
    for num in lista2:
        vac += str(num)
    return int(vac)
