def tower_builder(n_floors, block_size):
    w, h = block_size
    filled_block = '*' * w
    empty_block = ' ' * w
    tower = []
    for n in range(1,n_floors+1):
        for _ in range(h):
            tower.append( empty_block * (n_floors - n) + filled_block * (2*n -1) + empty_block * (n_floors - n))
    return tower
