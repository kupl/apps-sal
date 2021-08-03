def row_weights(array):
    counter_1 = 0
    counter_2 = 0

    for x in range(len(array)):
        if x % 2 == 0:
            counter_1 += array[x]
        else:
            counter_2 += array[x]
    return (counter_1, counter_2)
