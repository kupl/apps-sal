def meters(x):
    (prefix, power) = next((pair for pair in zip('YZEPTGMk', range(24, 0, -3)) if x >= 10 ** pair[1]), ('', 0))
    return '{:g}{}m'.format(x / 10 ** power, prefix)
