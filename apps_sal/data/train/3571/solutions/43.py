# Input: size of the wall, size of each pixels (both in milimeters)
# Output: whether we can fit an integer number of pixels in the wall
# Strategy: check whether the remainder of wall_length divided by pixel_size is 0
def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0
