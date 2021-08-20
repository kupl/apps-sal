def how_much_water(l, x, n):
    return 'Too much clothes' if n > 2 * x else 'Not enough clothes' if n < x else round(1.1 ** (n - x) * l, 2)
