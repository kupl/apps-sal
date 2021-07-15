import math

def power_of_two(x):
    if x == 1:
        return True
    elif x < 1 or x % 2:
        return False
    return power_of_two(x//2)
