def is_divisible(wall_length, pixel_size):
    remainder = wall_length % pixel_size
    return (remainder == 0)


is_divisible(4066, 27)
