def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0


# Your function should take two arguments:
    # The size of the wall in millimiters
    # The size of a pixel in millimeters
    # It should return True if you can fit
    # an exact number of pixels on the wall
    # Otherwise it should return False
# For example, is_divisble(4050, 27) should return True
