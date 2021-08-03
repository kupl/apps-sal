import math


def power_of_two(x):
    if x <= 0:
        return False
    if x > 0:
        y = int((math.log(x, 2)))
        for i in range(y - 1, y + 2):
            if 2**i == x:
                return True

        return False
