import math


def is_divisible(wall_length, pixel_size):
    # Your code here.
    division = (wall_length % pixel_size)
    #ddivision = (wall_length % pixel_size)
    return int(division) == 0.0 and float(division) >= 0.0
