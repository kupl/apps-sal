def sc(width, length, gaps):
    perimeter = 2 * (width + length - 2)
    (trees, remainder) = divmod(perimeter, gaps + 1)
    return remainder == 0 and trees
