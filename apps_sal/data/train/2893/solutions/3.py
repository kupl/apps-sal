import math
def plant_doubling(n):
    times = 0
    while n != 0:
        times += 1
        n = n - (2 ** int(math.log(n, 2)))
    return times
