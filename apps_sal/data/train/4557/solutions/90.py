def row_weights(array):
    a = sum(array[i] for i in range(len(array)) if i % 2 == 0)
    b = sum(array[i] for i in range(len(array)) if i % 2 != 0)
    return (a, b)
