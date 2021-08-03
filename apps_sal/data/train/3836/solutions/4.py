def factors(x):
    return -1 if type(x) != int or x < 1 else \
        [n for n in range(x, 0, -1) if x % n == 0]
