def is_divisible(wall_length, pixel_size):
    return {0: True}.get(wall_length % pixel_size, False)

