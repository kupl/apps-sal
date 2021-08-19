def array_change(a):
    c = 0
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:
            c += a[i - 1] - a[i] + 1
            a[i] = a[i - 1] + 1
    return c
