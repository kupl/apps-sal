import math
def power_of_two(x):
    if x == 0:
        return False
    check = int(math.log(x, 2))
    if 2 ** check == x:
        return True
    return False
