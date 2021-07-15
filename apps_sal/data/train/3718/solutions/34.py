def divisors(n):
    return sum(n % a == 0 for a in range(1, n + 1))

