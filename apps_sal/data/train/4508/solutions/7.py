def is_vampire(x, y):
    return sorted(f'{x}{y}') == sorted(f'{x * y}') and x % 10 + y % 10 > 0


vampires = [None] + sorted({x * y for p in (1, 2) for x in range(10 ** p, 10 ** (p + 1)) for y in range(x, 10 ** (p + 1)) if is_vampire(x, y)})
VampireNumber = vampires.__getitem__
