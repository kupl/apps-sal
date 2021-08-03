def matrix_mult(a, b):
    b = list(zip(*b))
    return [[sum(n * m for n, m in zip(a[x], b[y])) for y in range(len(a))] for x in range(len(a))]
