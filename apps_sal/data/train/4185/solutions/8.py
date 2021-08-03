def sc(width, length, gaps):
    n = 2 * (length + (width - 2))
    return n / (gaps + 1) if n % (gaps + 1) == 0 else 0
