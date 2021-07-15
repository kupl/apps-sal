def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix))) if len(matrix) > 0 and len(matrix[0]) == len(matrix) else None
