def different_squares(matrix):
    h, w = len(matrix), len(matrix[0]) if matrix else 0
    return len(set(((matrix[i][j], matrix[i][j+1]), (matrix[i+1][j], matrix[i+1][j+1]))  for i in range(h-1) for j in range(w-1)))

