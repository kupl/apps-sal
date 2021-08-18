def chameleon(chameleons, desiredColor):
    a, b, c = chameleons[desiredColor:] + chameleons[:desiredColor]
    if b < c:
        b, c = c, b
    if (b - c) % 3 != 0 or a < (b - c) / 3:
        return -1
    return b
