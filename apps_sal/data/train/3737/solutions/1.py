def calc(a):
    for i, n in enumerate(a):
        if a[i] > 0:
            a[i] *= a[i]
        if i % 3 == 2:
            a[i] = a[i] * 3
        if i % 5 == 4:
            a[i] = a[i] * -1
    return sum(a)
