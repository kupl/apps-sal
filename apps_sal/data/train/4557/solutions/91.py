def row_weights(a):
    first = 0
    second = 0
    for i in range(len(a)):
        if i % 2 == 0:
            first += a[i]
        else:
            second += a[i]
    return (first, second)
