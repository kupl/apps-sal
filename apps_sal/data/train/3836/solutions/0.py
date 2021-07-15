def factors(x):
    if not isinstance(x, int) or x < 1:
        return -1
    return [i for i in range(x, 0, -1) if x % i == 0]

