import math

def bouncing_ball(initial, proportion):
    return math.ceil(math.log(initial, 1/proportion))
