def is_divisible(wall_length, pixel_length):
    integer_multiple = wall_length % pixel_length
    return integer_multiple == 0
