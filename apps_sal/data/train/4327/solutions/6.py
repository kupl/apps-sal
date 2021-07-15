def chameleon(chameleons, desiredColor):
    # rotate a, b, c as a: desiredColor and b ≥ c
    a, b, c = chameleons[desiredColor:] + chameleons[:desiredColor]
    if b < c:
        b, c = c, b
    # combine a and b to become c x times so that b - x = c + 2x i.e. 3x = b - c
    if (b - c) % 3 != 0 or a < (b - c) / 3:
        return -1
    # combine b and c to become a for (b - x) times or (c + 2x) times
    # total number of combinations = x + b - x = b
    return b
