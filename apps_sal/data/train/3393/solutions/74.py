import math


def div(n):
    i = 1
    l = []
    m = []
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                l.append(i)
                m.append(i ** 2)
            else:
                l.append(i)
                l.append(n // i)
                m.append(i ** 2)
                m.append((n // i) ** 2)
        i = i + 1
    if math.sqrt(sum(m)).is_integer():
        return [n, sum(m)]
    pass


def list_squared(m, n):
    b = []
    for j in range(m, n):
        if div(j):
            b.append(div(j))
    return b
