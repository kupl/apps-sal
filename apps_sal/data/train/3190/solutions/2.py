PRIMES = set([str(num) for num in range(3, 100) if all(num % x != 0 for x in [2] + list(range(3, int(num ** 0.5) + 1, 2)))])


def solve(a, b):
    return sum(1 for x in range(max(a, 1000), b) if x % 100 == x * x % 100 and str(x)[:2] in PRIMES and str(x * x)[:2] in PRIMES)
