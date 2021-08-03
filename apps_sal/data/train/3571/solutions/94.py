def is_divisible(wall_length, pixel_size):
    x = (wall_length / pixel_size)
    y = (wall_length // pixel_size)
    return (x == y)
