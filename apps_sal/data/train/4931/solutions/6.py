def different_squares(matrix):
    squares = []
    for r in range(len(matrix) - 1):
        for c in range(len(matrix[0]) - 1):
            squares.append((matrix[r][c], matrix[r][c + 1], matrix[r + 1][c], matrix[r + 1][c + 1]))
    unique = set(squares)
    return len(unique)
