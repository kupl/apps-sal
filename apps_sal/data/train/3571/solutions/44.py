def is_divisible(wall_length, pixel_size):
    precise = wall_length % pixel_size
    return precise == 0
