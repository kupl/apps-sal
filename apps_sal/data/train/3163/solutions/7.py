a = [i * (i + 1) // 2 for i in range(211)]
b = [i**2 + j**2 for i, j in zip(a, a[1:])]


def triangular_sum(n):
    return n in b
