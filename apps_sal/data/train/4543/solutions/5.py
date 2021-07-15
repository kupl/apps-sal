def shades_of_grey(n):
    if n <= 0:
        return []
    return ['#{0:02x}{0:02x}{0:02x}'.format(n) for n in range(1, min(n, 254) + 1)]
