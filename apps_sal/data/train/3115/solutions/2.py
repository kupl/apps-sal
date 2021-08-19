def diagonal_sum(array):
    return sum([array[a][a] for a in range(len(array))])
