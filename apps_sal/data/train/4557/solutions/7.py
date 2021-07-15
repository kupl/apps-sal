def row_weights(array):
    return sum(x for i, x in enumerate(array) if not i % 2), sum(x for i, x in enumerate(array) if i % 2)
