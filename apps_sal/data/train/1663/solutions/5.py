def count_divisors(n):
    sq = int(n**.5)
    return 2 * sum(n // i for i in range(1, sq + 1)) - sq**2
