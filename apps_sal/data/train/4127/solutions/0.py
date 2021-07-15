def count_pairs_int(d, m):
    return sum(1 for i in range(1, m - d) if divisors(i) == divisors(i + d))

def divisors(n):
    return sum(1 + (n // k != k) for k in range(1, int(n**0.5) + 1) if n % k == 0)

