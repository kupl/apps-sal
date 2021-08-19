def diagonal_sum(array):
    return sum((row[i] for (i, row) in enumerate(array)))
