import math

def power_of_two(x):
    return False if x == 0 else True if math.pow(2, round(math.log(x, 2))) == x else False
