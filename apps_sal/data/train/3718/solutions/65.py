def divisors(n):
    return sum([1 if n % x == 0 else 0 for x in range(1,n)]) + 1
