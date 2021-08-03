def calc(a):
    return sum([i * (i if i > 0 else 1) * (3 if k % 3 == 2 else 1) * (-1 if k % 5 == 4 else 1) for k, i in enumerate(a)])
