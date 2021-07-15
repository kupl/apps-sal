def row_weights(array):

    one = [array[i] for i in range(0, len(array), 2)]
    two = [array[i] for i in range(1, len(array), 2)]

    return sum(one), sum(two)
