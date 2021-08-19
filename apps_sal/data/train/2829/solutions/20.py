def array_madness(a, b):
    lista1 = []
    lista2 = []
    for num1 in a:
        num1 = num1 ** 2
        lista1.append(num1)
    add_lista1 = sum(lista1)
    for num2 in b:
        num2 = num2 ** 3
        lista2.append(num2)
    add_lista2 = sum(lista2)
    if add_lista1 > add_lista2:
        return True
    else:
        return False
