def reverse_on_diagonals(matrix):
    n = len(matrix)
    for i in range(n // 2):
        matrix[i][i], matrix[n - i - 1][n - i - 1] = matrix[n - i - 1][n - i - 1], matrix[i][i]

        matrix[i][n - i - 1], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][n - i - 1]

    return matrix
