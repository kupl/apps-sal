def is_divisible(wall_length, pixel_size):
    a = wall_length % pixel_size
    if a == 0:
        return True
    else:
        return False
