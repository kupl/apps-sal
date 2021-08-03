# player moves from left to right
# The player rolls the dice and moves the number of spaces indicated by the dice two times.
# input - two integers
# output - integer

# edge cases - die roll can only be (1-6), no numbers given

# sample test (2, 7) = 16
# 2 + (7 * 2)

def move(position, roll):
    return (roll * 2) + position
