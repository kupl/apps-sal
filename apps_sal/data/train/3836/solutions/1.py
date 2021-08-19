def factors(x):
    if not isinstance(x, int) or x < 1:
        return -1
    return sorted({j for i in range(1, int(x ** 0.5) + 1) if x % i == 0 for j in [i, x // i]}, reverse=True)
