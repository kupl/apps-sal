import math


def am_i_wilson(P):
    if P < 2:
        return False
    else:
        for x in range(2, P):
            if P % x == 0:
                return False
        if ((math.factorial(P - 1)) + 1) % (P * P) == 0:
            return True
        else:
            return False
