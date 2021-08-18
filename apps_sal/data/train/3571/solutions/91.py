def is_divisible(wall_length, pixel_size):
    is_div = wall_length % pixel_size
    return is_div == 0


print(is_divisible(4050, 27))
