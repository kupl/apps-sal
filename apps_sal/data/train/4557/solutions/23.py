def row_weights(array):
    return sum(n for i, n in enumerate(array) if i % 2 == 0), sum(n for i, n in enumerate(array) if i % 2)
