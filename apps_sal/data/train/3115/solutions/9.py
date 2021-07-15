def diagonal_sum(array):
    sum = 0
    for n in range(len(array)):
        sum += array[n][n]
    return sum
