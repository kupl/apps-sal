c = {1: 1}


def F(n):
    if n in c:
        return c[n]
    c[n] = 1 + F(n * 3 + 1 if n & 1 else n // 2)
    return c[n]


def max_collatz_length(n):
    return [] if type(n) != int or n <= 0 else max([[i, F(i)] for i in range(1, n + 1)], key=lambda x: x[1])
