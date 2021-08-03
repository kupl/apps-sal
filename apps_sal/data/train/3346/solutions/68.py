import math


def gap(g, m, n):
    prime = 1
    for i in range(m, n):
        primeFlag = True
        for j in range(2, math.floor(math.sqrt(i) + 1)):
            if i % j == 0:
                primeFlag = False

        if primeFlag:  # if i prime
            if 1 != prime and i - prime == g:
                return [prime, i]
            else:
                prime = i
    return None
    # your code
