def peak_height(mountain):
    neighbours = lambda z: {z + 1j ** d for d in range(4)}
    mountain = {x + 1j * y for x, r in enumerate(mountain)
                           for y, c in enumerate(r) if c == '^'}
    height, base = 0, set().union(*map(neighbours, mountain)) - mountain
    while mountain:
        height += 1
        base = set.union(*map(neighbours, base)) & mountain
        mountain -= base
    return height
