def row_weights(array):
    return (sum((j for (i, j) in enumerate(array) if i % 2 == 0)), sum((j for (i, j) in enumerate(array) if i % 2 != 0)))
