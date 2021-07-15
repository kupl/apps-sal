def row_weights(array):
    total_weights_even = 0
    total_weights_odd = 0
    for i in range(0, len(array), 2):
        total_weights_even += array[i]
    for j in range(1, len(array), 2):
        total_weights_odd += array[j]
    return (total_weights_even, total_weights_odd)
