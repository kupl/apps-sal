def shades_of_grey(n):
    if n > 254:
        n = 254
    return ['#%02x%02x%02x' % (i, i, i) for i in range(1, n + 1)]
