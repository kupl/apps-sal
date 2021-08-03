def tower_builder(n_floors, block_size):
    w, h = block_size
    tower = ['*' * (2 * n_floors - 1) * w] * h
    base = tower[-1]
    for f in range(1, n_floors):
        base = base[:len(base) - 2 * w]
        tower += [' ' * w * f + base + ' ' * w * f] * h
    return tower[::-1]
