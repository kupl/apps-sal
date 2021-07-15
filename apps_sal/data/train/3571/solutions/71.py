def is_divisible(wall_length, pixel_size):
    div = wall_length / pixel_size
    div_floor = wall_length // pixel_size
    return div == div_floor
