import math


def max_multiple(divisor, bound):
    if bound % divisor == 0:
        return bound
    else:
        nearestFactor = math.floor(bound / divisor)
        return divisor * nearestFactor
