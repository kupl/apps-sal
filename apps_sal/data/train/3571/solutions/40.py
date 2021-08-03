def is_divisible(wall_length, pixel_size):
    # Your code here.
    fit_wall = wall_length % pixel_size
    return fit_wall == 0
