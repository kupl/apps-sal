def is_divisible(wall_length, pixel_size):
    # Your code here.
    paul = wall_length % pixel_size == 0
    return paul
    print(is_divisible(4050, 27))
