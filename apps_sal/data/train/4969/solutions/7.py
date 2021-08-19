def tower_builder(n_floors, block_size):
    (W, H) = block_size
    (result, maxi) = ([], (2 * n_floors - 1) * W)
    for i in range(W, maxi + 1, 2 * W):
        result.extend([('*' * i).center(maxi)] * H)
    return result
