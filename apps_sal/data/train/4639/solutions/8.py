def power_of_two(x):
    from math import log2, pow
    if not x == 0:
        c = log2(x)
        return c%1 == 0 and pow(2,c) == x #precision here breaks so assume false
    else: 
        return False
