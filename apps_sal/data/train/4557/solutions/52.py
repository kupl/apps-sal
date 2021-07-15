def row_weights(array):
    sum1 = sum([array[i] for i in range(len(array)) if i % 2 == 0])
    sum2 = sum([array[i] for i in range(len(array)) if i % 2 != 0])
    return (sum1,sum2)
