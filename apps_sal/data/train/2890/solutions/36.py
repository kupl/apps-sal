import math

def multiples(m, n):
    list = []
    i = 1
    while i <= m:
        list.append(n*i)
        i += 1
    return list
