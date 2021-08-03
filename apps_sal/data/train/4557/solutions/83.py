def row_weights(array):
    first, second = 0, 0
    for i, el in enumerate(array, 1):
        if i % 2 == 0:
            first += el
        else:
            second += el
    return (second, first)
