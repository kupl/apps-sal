def is_divisible(wall_length, pixel_size):
    # Your code here.
    a = wall_length / pixel_size
    b = wall_length  // pixel_size
    if a == b:
        return True
    else:
        return False

