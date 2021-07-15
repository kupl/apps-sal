def row_weights(array):
    return (sum(n for i, n in enumerate(array) if not i % 2), sum(n for i, n in enumerate(array) if i % 2))
