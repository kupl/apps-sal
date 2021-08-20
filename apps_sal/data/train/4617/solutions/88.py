import math


def powers_of_two(n):
    rez = []
    i = 0
    while i <= n:
        rez.append(math.pow(2, i))
        i += 1
    return rez
