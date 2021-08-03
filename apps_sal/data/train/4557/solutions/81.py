def row_weights(array):
    w1 = sum(array[i] for i in range(len(array)) if i % 2 == 0)
    w2 = sum(array[i] for i in range(len(array)) if i % 2 == 1)
    return w1, w2
