def reverse_on_diagonals(matrix):
    diag1 = [matrix[i][i] for i in range(len(matrix))]
    diag2 = [matrix[i][~i] for i in range(len(matrix))]
    for i, n in enumerate(reversed(diag1)):
        matrix[i][i] = n
    for i, n in enumerate(reversed(diag2)):
        matrix[i][~i] = n
    return matrix
