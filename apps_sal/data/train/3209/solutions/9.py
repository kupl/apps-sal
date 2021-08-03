def find_unknown_number(x, y, z):
    r = z if z > 0 else 7
    while r % 3 != x or r % 5 != y or r % 7 != z:
        r = r + 7

    return r
