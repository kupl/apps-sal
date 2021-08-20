def how_much_water(w, l, c):
    if l * 2 < c:
        return 'Too much clothes'
    elif l > c:
        return 'Not enough clothes'
    else:
        return round(w * 1.1 ** (c - l), 2)
