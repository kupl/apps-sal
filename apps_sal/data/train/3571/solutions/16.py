def is_divisible(wall_length, pixel_size):
    while wall_length % pixel_size == 0:
        return True
    else:
        return False
