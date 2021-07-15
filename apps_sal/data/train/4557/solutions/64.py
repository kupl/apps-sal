def row_weights(array):
    total_weights_even = 0
    total_weights_odd = 0
    for i in range(len(array)):
        if i % 2 == 0:
            total_weights_even += array[i]
        else:
            total_weights_odd += array[i]
    return (total_weights_even, total_weights_odd)
