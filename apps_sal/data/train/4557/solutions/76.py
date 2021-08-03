def row_weights(array):
    sum1 = sum2 = 0
    for i in range(len(array)):
        if i % 2 == 0:
            sum1 = sum1 + array[i]
        else:
            sum2 = sum2 + array[i]
    return (sum1, sum2)
