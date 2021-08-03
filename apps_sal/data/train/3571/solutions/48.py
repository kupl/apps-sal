def is_divisible(wall_length, pixel_size):
    calculate = wall_length % pixel_size == 0
    return calculate


print(is_divisible)
