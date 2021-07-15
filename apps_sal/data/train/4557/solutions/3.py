def row_weights(array):
    a = array[::2]
    b = array[1::2]
    return sum(a),sum(b)
