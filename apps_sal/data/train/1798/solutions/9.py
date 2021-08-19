import numpy as np


def next_gen(grid):
    neighbours = np.array([np.roll(grid, (i, j), axis=(0, 1)) for i in [-1, 0, 1] for j in [-1, 0, 1]]).sum(axis=0) - grid
    return (neighbours == 3) | grid & (neighbours == 2)


def unpad(grid):
    if grid[0, ].sum() == 0:
        return unpad(grid[1:])
    if grid[-1, ].sum() == 0:
        return unpad(grid[:-1])
    if grid[:, 0].sum() == 0:
        return unpad(grid[:, 1:])
    if grid[:, -1].sum() == 0:
        return unpad(grid[:, :-1])
    return grid


def get_generation(cells, generations):
    cells = np.array(cells)
    for _ in range(generations):
        cells = next_gen(np.pad(cells, 1, mode='constant'))
    return unpad(cells).tolist()
