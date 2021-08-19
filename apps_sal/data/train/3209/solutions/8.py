def find_unknown_number(x, y, z):
    return 105 if x + y + z == 0 else (set(range(x, 106, 3)) & set(range(y, 106, 5)) & set(range(z, 106, 7))).pop()
