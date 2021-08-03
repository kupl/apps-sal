def is_divisible(wall_length, pixel_size):
    wall = wall_length
    wall %= pixel_size
    return(wall == 0)


print(is_divisible(6, 2))
