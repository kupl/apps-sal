def divisors(n):

    return len([x for x in range(1, n + 1, 1) if (n / x).is_integer()])
