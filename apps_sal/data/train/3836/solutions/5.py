def factors(n):
    from math import sqrt
    if not isinstance(n, int) or n < 1:
        return -1
    lim = int(sqrt(n))
    divisors = set([n, 1])
    start = 2 + n % 2
    step = start - 1
    for i in range(start, lim + 1, step):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors, reverse=True)
