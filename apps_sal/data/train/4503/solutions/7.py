def f(n):
    x = [2**i for i in range(n + 1)]
    x.append(2**(n + 1) - 1)
    return x
