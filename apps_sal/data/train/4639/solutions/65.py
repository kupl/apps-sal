from math import log
def power_of_two(x):
    if x < 1: return False
    if str(x)[-1:] in '13579' and x>1: return False
    else:
        return 2**int(log(x,2)) == x
