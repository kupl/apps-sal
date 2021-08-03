import math


def is_divisible(wall_length, pixel_size):
    return wall_length / pixel_size == math.floor(wall_length / pixel_size)
