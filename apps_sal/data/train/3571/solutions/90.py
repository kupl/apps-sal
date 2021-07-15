def is_divisible(wall_length, pixel_size):
    # Your code here.
    remdr = wall_length%pixel_size
    print(remdr)
    return remdr==0
