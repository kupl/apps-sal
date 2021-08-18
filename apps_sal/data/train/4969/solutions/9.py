import math


def tower_builder(n_floors, block_size):
    w, h = block_size
    stars = w
    height_count = 0
    tower = []
    for i in range(n_floors * h):
        ground_floor_stars = w * 2 * n_floors - w
        spaces = " " * int((ground_floor_stars - stars) / 2)
        floor = spaces + '*' * stars + spaces
        tower.append(floor)
        height_count += 1
        if height_count == h:
            stars += w * 2
            height_count = 0
    return tower
