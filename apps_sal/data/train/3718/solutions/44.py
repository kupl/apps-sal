def divisors(n):
    return len(list(i for i in range(n) if n % (i + 1) == 0))
