def trace(matrix):
    if matrix and {len(matrix)} == {len(m) for m in matrix}:
        return sum((matrix[i][i] for i in range(len(matrix))))
