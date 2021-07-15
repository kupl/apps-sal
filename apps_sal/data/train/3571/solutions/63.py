def is_divisible(wall_length, pixel_size):
    modulus = wall_length % pixel_size
    return modulus == 0
