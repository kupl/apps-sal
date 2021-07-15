def row_weights(array):
    return (sum(array[0::2]), sum(array[1::2])) if len(array) > 1 else (array[0], 0)
