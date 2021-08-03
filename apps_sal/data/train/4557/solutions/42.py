def row_weights(array):
    a = 0
    b = 0
    for i, e in enumerate(array):
        if i % 2 == 0:
            a += e
        else:
            b += e
    return (a, b)
