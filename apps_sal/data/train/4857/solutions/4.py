def square_up(n):
    x = list(range(n, 0, -1))
    y = [[0] * i + x[i:] for i in range(n - 1, -1, -1)]
    return [i for l in y for i in l]
