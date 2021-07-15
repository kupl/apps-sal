def is_divisible(wall_length, pixel_size):
    n = wall_length / pixel_size
    return n % 2 == 0 or n % 2 == 1.0
