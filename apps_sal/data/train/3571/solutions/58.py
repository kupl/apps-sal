def is_divisible(wall_length, pixel_size):
    # Your code here.
    ts = wall_length % pixel_size
    return ts == 0
