def trace(matrix):
    if matrix and len(matrix) == len(matrix[0]):
        return sum(row[i] for i, row in enumerate(matrix))
