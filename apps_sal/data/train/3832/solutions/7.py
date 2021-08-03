def all_permuted(array_length):
    a = [1, 0]
    for x in range(2, array_length + 1):
        a[0], a[1] = a[1], (x - 1) * (a[1] + a[0])
    return a[1]
