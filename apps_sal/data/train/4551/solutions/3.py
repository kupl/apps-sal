def score_matrix(matrix):
    return sum((sum((el if (row_idx + col_idx) % 2 == 0 else -el for (col_idx, el) in enumerate(row))) for (row_idx, row) in enumerate(matrix)))
