def square(number):
    lista = [1]
    for n in range(1, number):
        result = lista[-1]*2
        lista.append(result)
    return lista[-1]
