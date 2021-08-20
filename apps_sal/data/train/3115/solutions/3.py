def diagonal_sum(array):
    return sum((row[idx] for (idx, row) in enumerate(array)))
