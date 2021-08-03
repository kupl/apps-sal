def row_sum_odd_numbers(n):
    lista = []
    licznik = 0

    for i in range(n + 1):
        licznik = licznik + i

    for i in range(licznik):
        x = (2 * i) + 1
        lista.append(x)

    return sum(lista[-n:])
