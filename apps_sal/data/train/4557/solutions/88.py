def row_weights(array):
    one = 0
    two = 0
    for (s, i) in enumerate(array, 1):
        if s % 2 == 0:
            two += i
        else:
            one += i
    return (one, two)
