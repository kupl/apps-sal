def get_divisors_sum(n):
    """Get the divisors: iterate up to sqrt(n), check if the integer divides n with r == 0
        Return the sum of the divisors squared."""
    divs = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.extend([i, int(n / i)])
    divs.extend([n])
    sm = sum([d ** 2 for d in list(set(divs))])
    return sm


def list_squared(m, n):
    """Search for squares amongst the sum of squares of divisors of numbers from m to n """
    out = []
    for j in range(m, n + 1):
        s = get_divisors_sum(j)
        if (s ** 0.5).is_integer():
            out.append([j, s])
    return out
