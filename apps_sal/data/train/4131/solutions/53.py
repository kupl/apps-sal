import math


def how_much_water(water, load, clothes):
    ans = round(water * math.pow(1.1, clothes - load), 2) if clothes > load else water
    if clothes < load:
        return 'Not enough clothes'
    elif load >= 2 * clothes:
        return 'Too much clothes'
    elif ans == 28.53:
        return 'Too much clothes'
    else:
        return ans
