def tower_builder(n_floors, block_size):
    w, h = block_size
    floors = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        for j in range(h):
            floors.append(' ' * n * w + '*' * (i * 2 + 1) * w + ' ' * n * w)

    return floors
