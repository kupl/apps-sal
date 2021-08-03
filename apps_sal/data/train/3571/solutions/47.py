def is_divisible(wall_length, pixel_size):
    i = wall_length % pixel_size
    if i == 0:
        return True
    else:
        return False
