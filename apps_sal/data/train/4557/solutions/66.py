def row_weights(array):
    return (sum((array[i] for i in range(0, len(array), 2))), sum((array[j] for j in range(1, len(array), 2))))
