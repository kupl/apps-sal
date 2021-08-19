def is_divisible(wall_length, pixel_size):
    a_w = wall_length ** 2
    a_p = pixel_size ** 2
    return True if a_w % a_p == 0 else False
