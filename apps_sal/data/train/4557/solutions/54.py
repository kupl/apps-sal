def row_weights(arr):
    a = 0
    b = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            b += arr[i]
        else:
            a += arr[i]
    return (b,a)
