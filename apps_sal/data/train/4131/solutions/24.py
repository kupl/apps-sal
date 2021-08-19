def how_much_water(L, X, N):
    if N > 2 * X:
        return 'Too much clothes'
    if N < X:
        return 'Not enough clothes'
    else:
        s = L * 1.1 ** (N - X)
        return round(s, 2)
