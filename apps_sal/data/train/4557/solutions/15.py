def row_weights(array):
    one, two = 0, 0
    for i, n in enumerate(array):
        if i % 2:
            two += n
        else:
            one += n
    return (one, two)
