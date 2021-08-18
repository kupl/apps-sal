def sc(width, length, gaps):
    a, b = divmod(2 * width + 2 * length - 4, gaps + 1)
    return 0 if b else a
