def row_weights(array):
    even = 0
    odd = 0
    for num in range(len(array)):
        if num % 2 == 0:
            even += array[num]

        else:
            odd += array[num]

    return even, odd
