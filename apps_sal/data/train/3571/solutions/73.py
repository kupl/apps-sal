def is_divisible(wall_length, pixel_size):
    # Your code here
    wall_n = wall_length
    pixel_n = pixel_size
    math = wall_n % pixel_n
    if math != 0:
        return False
    elif math == 0:
        return True
