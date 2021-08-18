def row_weights(array):
    total1 = 0
    total2 = 0
    for x in range(len(array)):
        if x % 2 == 1:
            total2 += array[x]
        else:
            total1 += array[x]
    return tuple((total1, total2))
