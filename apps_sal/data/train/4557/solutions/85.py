def row_weights(array):
    sum1 = 0
    sum2 = 0

    for idx, i in enumerate(array):
        if idx % 2 == 0:
            sum1 += i
        else:
            sum2 += i

    return (sum1, sum2)
