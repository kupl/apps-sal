def is_divisible(wall_length, pixel_size):
    division_remainder = wall_length % pixel_size
    return division_remainder == 0
