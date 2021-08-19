import math


def not_visible_cubes(n):
    if (n < 2):
        return 0
    else:
        #         return long(math.pow(n-2,3))
        return (n - 2) * (n - 2) * (n - 2)
