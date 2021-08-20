def reverse_on_diagonals(matrix):
    diagonals = [(row[idx], row[-idx - 1]) for (idx, row) in enumerate(matrix)]
    for (idx, ch) in enumerate(reversed(diagonals)):
        (matrix[idx][idx], matrix[idx][-idx - 1]) = ch
    return matrix
