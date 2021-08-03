def array_madness(a, b):
    for i, v in enumerate(a):
        a[i] = v**2
    for i, v in enumerate(b):
        b[i] = v**3
    return sum(a) > sum(b)
