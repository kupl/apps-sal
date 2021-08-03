from itertools import chain, repeat


def find(n):
    if n <= 3:
        return [0, 1, 2, 2][n]
    inicio, suma, largo = [[2]], 5, 4
    for i, j in enumerate(chain.from_iterable(inicio), 3):
        suma += i * j
        if suma >= n:
            x = (suma - n) // i
            return j + largo - x - 1
        inicio.append(repeat(i, j))
        largo += j
