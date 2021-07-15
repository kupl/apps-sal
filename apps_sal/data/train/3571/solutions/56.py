def is_divisible(wall_length, pixel_size):
    # Your code here.
    wall_length_true = wall_length
    wall_length_true /= pixel_size
    wall_length_floor = wall_length
    wall_length_floor //= pixel_size
    wall_length_true %= wall_length_floor
    return wall_length_true == 0
