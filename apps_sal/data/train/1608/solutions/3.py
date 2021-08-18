def determinant(matrix):
    result = 0
    l = len(matrix)

    if l == 1:
        return matrix[0][0]

    if l == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    for j in range(0, l):
        if l != 2:
            sub_matrix = []
            sub_matrix = [(row[0:j] + row[j + 1:]) for row in matrix[1:]]
        result = result + (-1)**j * matrix[0][j] * determinant(sub_matrix)
    return result
