def how_much_water(w, l, c):
    print(w, l, c)
    if c > 2 * l:
        return 'Too much clothes'
    if c < l:
        return 'Not enough clothes'
    return round(w * 1.1 ** (c - l), 2)
