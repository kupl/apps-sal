def max_multiple(divisor, bound):
    lista = [i for i in range(1, bound + 1)]
    lista.reverse()
    for i in lista:
        if i % divisor == 0:
            return i
