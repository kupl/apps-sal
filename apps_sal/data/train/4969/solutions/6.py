def tower_builder(n_floors, block_size):
    w, h = block_size
    return [(n_floors * w - i * w) * " " + (i * w * 2 - w) * "*" + (n_floors * w - i * w) * " " for i in sorted(list(range(1, n_floors + 1)) * h)]
