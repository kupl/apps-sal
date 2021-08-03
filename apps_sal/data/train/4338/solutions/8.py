def reverse_on_diagonals(matrix):
    for i in range(int(len(matrix) / 2)):
        matrix[i][i], matrix[len(matrix) - 1 - i][len(matrix) - 1 - i] = matrix[len(matrix) - 1 - i][len(matrix) - 1 - i], matrix[i][i]
        matrix[len(matrix) - 1 - i][i], matrix[i][len(matrix) - 1 - i] = matrix[i][len(matrix) - 1 - i], matrix[len(matrix) - 1 - i][i]
    return matrix
