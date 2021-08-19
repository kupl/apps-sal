def row_weights(array):
    return (sum((array[x] for x in range(0, len(array)) if x % 2 == 0)), sum((array[x] for x in range(0, len(array)) if x % 2 != 0)))
