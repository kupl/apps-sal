def row_weights(array):
    t1, t2 = 0, 0
    for i in range(len(array)):
        if i % 2:
            t2 += array[i]
        else:
            t1 += array[i]
    return t1, t2
