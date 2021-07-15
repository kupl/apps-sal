def different_squares(matrix):
    return len(set(tuple(tuple(row[j:j+2]) for row in matrix[i:i+2]) for i in range(len(matrix)-1) for j in range(len(matrix[0])-1)))
