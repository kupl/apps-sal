def count_divisors(n): # http://oeis.org/A006218
    sq = int(n ** .5)
    return 2 * sum(n // i for i in range(1, sq + 1)) - sq * sq
