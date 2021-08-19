def is_divisible(wall_length, pixel_size):
    # Your code here.def is_divisible(quotient, divisor)
    is_div = wall_length % pixel_size
    return is_div == 0


print(is_divisible(4050, 27))
