def row_weights(array):
    if len(array) == 1:
        return (array[0], 0)
    one = 0
    two = 0
    for i in range(len(array)):
        if i % 2 == 0:
            one += array[i]
        else:
            two += array[i]
    return (one, two)
