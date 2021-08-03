def row_weights(array):
    res = 0
    res2 = 0
    for i in range(len(array)):
        if i % 2 != 0:
            res += array[i]
        elif i % 2 == 0:
            res2 += array[i]
    return (res2, res)
