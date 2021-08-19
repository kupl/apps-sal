def is_divisible(wall_length, pixel_size):
    # if the wall length divided by the pixel size has a remainder of 0, there can be an exact fit of pixels
    return wall_length % pixel_size == 0
