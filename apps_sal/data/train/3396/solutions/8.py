def matrix_addition(a, b):
    result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    return result
