def matrix_mult(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(a))) for j in range(len(a))] for i in range(len(a))]
