def row_weights(array):
    first = [0]
    second = [0]
    for i in range(0, len(array)):
        if i % 2 == 0:
            first.append(array[i])
        else:
            second.append(array[i])
    return (sum(first), sum(second))
