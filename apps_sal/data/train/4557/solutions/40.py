def row_weights(array):
    a = array[::2]
    ba = array[1::2]
    return (sum(a), sum(ba))
