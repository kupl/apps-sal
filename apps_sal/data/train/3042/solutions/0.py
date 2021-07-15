def trace(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return None
    return sum(matrix[i][i] for i in range(len(matrix)))
