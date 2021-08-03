def squares_needed(grains, b=1, c=0):
    if c == 0:
        b = 1
    else:
        b *= 2
    if grains <= 0:
        return c
    c += 1

    return squares_needed(grains - b, b, c)
    return c
