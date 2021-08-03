def matrix_addition(a, b):
    for row in range(len(a)):
        for index in range(len(a)):
            a[row][index] += b[row][index]
    return a
