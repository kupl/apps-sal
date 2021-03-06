import math


def gap(g, m, n):
    if m % 2 == 0:
        m = m + 1
    lastprime = float('-inf')
    for i in range(m, n + 1, 2):
        lim = math.ceil(math.sqrt(i)) + 1
        isPrime = True
        for j in range(3, lim):
            if i % j == 0:
                isPrime = False
                break
        if not isPrime:
            continue
        elif i - lastprime == g:
            return [lastprime, i]
        else:
            lastprime = i
    return None
