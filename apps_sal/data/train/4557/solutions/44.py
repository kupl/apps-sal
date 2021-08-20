def row_weights(array):
    arr = [0, 0]
    for i in range(len(array)):
        if i % 2 == 0:
            arr[0] += array[i]
        else:
            arr[1] += array[i]
    return (arr[0], arr[1])
