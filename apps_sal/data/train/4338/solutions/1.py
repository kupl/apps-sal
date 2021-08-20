def reverse_on_diagonals(matrix):
    l = len(matrix)
    for i in range(l // 2):
        j = l - i - 1
        (matrix[i][i], matrix[j][j]) = (matrix[j][j], matrix[i][i])
        (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j])
    return matrix
