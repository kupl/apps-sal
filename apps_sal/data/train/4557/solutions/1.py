def row_weights(array):
    evens = sum(i for index, i in enumerate(array) if index % 2 == 0)
    return (evens, sum(array) - evens)
