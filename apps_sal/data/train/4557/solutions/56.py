def row_weights(array):
    first = 0
    second = 0
    for (i, weight) in enumerate(array):
        if i % 2 == 0:
            first += weight
        else:
            second += weight
    return (first, second)
