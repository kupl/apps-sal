def how_much_water(L, X, N):
    if N < X:
        return 'Not enough clothes'
    elif N > 2 * X:
        return 'Too much clothes'
    else:
        return round(L * 1.1 ** (N - X), 2)
