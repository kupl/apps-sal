import math


def gap(g, m, n):
    if m % 2 == 0:
        m = m + 1
    lastprime = float("-inf")

    for i in range(m, n + 1, 2):  # skip all even numbers
        # find factors
        lim = math.ceil(math.sqrt(i)) + 1
        isPrime = True
        for j in range(3, lim):
            if i % j == 0:
                isPrime = False
                break

        if not isPrime:
            continue  # skip this number if it isn't prime
        else:
            if i - lastprime == g:
                return [lastprime, i]
            else:
                lastprime = i

    return None
