def clonewars(n):
    return [2**max(0, n - 1), sum((n - i) * 2**i for i in range(0, n))]
