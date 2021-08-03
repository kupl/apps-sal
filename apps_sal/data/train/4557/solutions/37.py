def row_weights(array):
    c = []
    a = 0
    b = 0
    for i in range(len(array)):
        if i == 0 or i % 2 == 0:
            a = a + array[i]
        else:
            b = b + array[i]
    c.append(a)
    c.append(b)
    return tuple(c)
