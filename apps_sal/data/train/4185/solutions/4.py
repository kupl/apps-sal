def sc(width, length, gaps):
    land = 2 * (width - 1) + 2 * (length - 1)
    (d, m) = divmod(land, gaps + 1)
    return 0 if m else d
