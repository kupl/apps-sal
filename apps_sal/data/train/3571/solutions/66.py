def is_divisible(wall_length, pixel_size):
    # Quotient must be interger - not floating point.
    # Need integer check.
    return wall_length % pixel_size == 0
