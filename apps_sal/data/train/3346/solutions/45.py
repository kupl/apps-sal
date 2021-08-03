import math


def is_prime(num):
    # I'm sure this could be optimized
    if num % 2 == 0:
        return False
    else:
        for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
    return True


def gap(g, m, n):
    gapcounter = 0
    first_prime = False
    fp = 0
    if m % 2 == 0:
        m += 1
    for i in range(m, n + 1, 2):
        if first_prime:
            gapcounter += 2
        if is_prime(i):
            if first_prime:
                if gapcounter == g:
                    return [fp, i]
                else:
                    fp = i
                    gapcounter = 0
            else:
                first_prime = True
                fp = i
                gapcounter = 0
    return None
