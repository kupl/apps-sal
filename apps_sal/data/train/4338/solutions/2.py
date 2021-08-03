def reverse_on_diagonals(matrix):
    # Modifies the matrix in place. Only way to get O(n)
    diag1 = [matrix[i][i] for i in range(len(matrix))]
    diag2 = [matrix[i][~i] for i in range(len(matrix))]
    for i, n in enumerate(reversed(diag1)):
        matrix[i][i] = n
    for i, n in enumerate(reversed(diag2)):
        matrix[i][~i] = n
    return matrix
