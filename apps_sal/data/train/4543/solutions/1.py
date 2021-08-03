def shades_of_grey(n):
    return ['#{0:02x}{0:02x}{0:02x}'.format(i + 1) for i in range(min(254, n))]
