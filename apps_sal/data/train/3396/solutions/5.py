def matrix_addition(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]
