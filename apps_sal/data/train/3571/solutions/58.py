def is_divisible(wall_length, pixel_size):
    ts = wall_length % pixel_size
    return ts == 0
