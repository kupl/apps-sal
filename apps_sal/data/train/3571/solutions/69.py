def is_divisible(wall_length, pixel_size):
    size = wall_length % pixel_size
    return size == 0
