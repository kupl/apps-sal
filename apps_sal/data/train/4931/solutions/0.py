def different_squares(matrix):
    s = set()
    (rows, cols) = (len(matrix), len(matrix[0]))
    for row in range(rows - 1):
        for col in range(cols - 1):
            s.add((matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]))
    return len(s)
