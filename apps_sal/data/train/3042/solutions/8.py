def trace(matrix):
    size = len(matrix)
    if not matrix or any((len(row) != size for row in matrix)):
        return None
    return sum((matrix[i][i] for i in range(size)))
