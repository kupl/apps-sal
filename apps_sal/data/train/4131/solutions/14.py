def how_much_water(L, X, N):
    # Good luck!
    return 'Too much clothes' if N > 2 * X else 'Not enough clothes' if N < X else round(L * (1.1**(N - X)), 2)
