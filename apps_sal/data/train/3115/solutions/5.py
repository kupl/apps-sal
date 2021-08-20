def diagonal_sum(array):
    sum = 0
    for x in range(len(array)):
        for y in range(len(array[x])):
            if x == y:
                sum = sum + array[x][y]
    return sum
