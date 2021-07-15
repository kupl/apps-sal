def crossing_sum(matrix, row, col):
    mat_tr = [[i[j]  for i in matrix] for j in range(len(matrix[0]))]
    return sum(matrix[row] + mat_tr[col]) - matrix[row][col]
