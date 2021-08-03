lucas_sieve = [2, 1, 3, 4, 7]


def lucasnum(n):
    neg, n = 1 if n >= 0 or n % 2 == 0 else -1, abs(n)
    return neg * lucas_expand(n)


def lucas_expand(n):
    l = len(lucas_sieve)
    while n >= l:
        lucas_sieve.append(lucas_sieve[l - 1] + lucas_sieve[l - 2])
        l = len(lucas_sieve)
    return lucas_sieve[n]
