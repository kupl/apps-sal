def matrix_addition(a, b):
    return [ [a[row][col] + b[row][col] for col in range(len(a[0]))]
                for row in range(len(a)) ]
