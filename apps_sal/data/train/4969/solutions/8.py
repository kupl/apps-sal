def tower_builder(n_floors, block_size):
    tower = list()
    w, h = block_size
    l = (2 * n_floors - 1) * w
    sp = int(l / 2 - w / 2)

    for i in range(n_floors):
        for j in range(h):
            tower.append(' ' * sp + '*' * (l - 2 * sp) + ' ' * sp)
        sp = sp - w

    return tower
