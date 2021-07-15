def row_weights(array):
    x = [sum([array[i] for i in range(len(array)) if i%2 == j]) for j in range(2)]
    if len(array) < 3:
        x = x[:2]
    return tuple(x)
