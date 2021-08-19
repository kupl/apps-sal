import math


def gap(g, m, n):
    lp = 0
    for i in range(m, n + 1):
        if isprime(i):
            if lp != 0:
                if i - lp == g:
                    return [lp, i]
            lp = i
    return None


def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
