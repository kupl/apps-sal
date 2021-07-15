def transpose(matrix):
    return [[row[i] for row in matrix] for i, col in enumerate(matrix[0])]
