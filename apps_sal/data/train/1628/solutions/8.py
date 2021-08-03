import math


def proper_fractions(n):
    divisors, final, unique, i = [], [], [], 1
    while i <= math.sqrt(n):
        if (n % i == 0):
            if (n / i == i):
                divisors.append(i)
            else:
                divisors.extend([i, n / i])
        i = i + 1
    divisors.sort()
    if len(divisors) <= 2:
        return n - 1
    divisors.pop(0), divisors.pop()
    for num, item in enumerate(divisors):
        for x in divisors[0:num]:
            if not(item % x):
                break
        else:
            unique.append(item)

    for num, item in enumerate(unique):
        cache = n / item
        for x in unique[0:num]:
            cache = cache - (cache / x)
        final.append(cache)
    return(n - sum(final))
