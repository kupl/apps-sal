def how_much_water(W, L, C):
    return 'Not enough clothes' if C < L else 'Too much clothes' if C > L * 2 else round(W * 1.1 ** (C - L), 2)
