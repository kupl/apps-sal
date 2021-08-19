#import math
#from decimal import *
def am_i_wilson(n):
    # if n > 1:
    #    return (Decimal(math.factorial(n-1) + 1) / n**2) % 1 == 0
    # else: return False

    return n in [5, 13, 563]
