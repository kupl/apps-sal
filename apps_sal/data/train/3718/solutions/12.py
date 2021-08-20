def divisors(n):
    return sum((not n % i for i in range(1, n + 1)))
