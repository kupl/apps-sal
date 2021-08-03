def productFib(prod):
    n, n_1 = 0, 1
    while True:
        if n * n_1 == prod:
            return [n, n_1, True]
        elif n * n_1 > prod:
            return [n, n_1, False]
        else:
            n, n_1 = n_1, n_1 + n
