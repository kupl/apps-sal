def row_weights(array):
    a, b = 0, 0
    for i in range(0, len(array), 2):
        a += array[i]
    for j in range(1, len(array), 2):
        b += array[j]
    return a, b
