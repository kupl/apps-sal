# You haven't decided on the dimensions of your piece, how large you want your pixels to be, or which wall you want to use. You just know that you want to fit an exact number of pixels.

#  tell you whether a wall of a certain length can exactly fit an integer number of pixels of a certain length.

# input - two integers (wall_length, pixel_size)
# output - boolean

# edge cases - decimals aren't allowed, only whole numbers, empty inputs aren't allowed

def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0
