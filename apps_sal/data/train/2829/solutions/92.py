def array_madness(a, b):
    x = y = i = 0
    for i in range(len(a)):
        x = x + a[i] * a[i]
    for i in range(len(b)):
        y = y + b[i] * b[i] * b[i]
    return x > y
