def solve(n, k):
    maxGcd = 2 * n // (k * (k + 1))
    for gcd in range(maxGcd, 0, -1):
        last = n - gcd * k * (k - 1) // 2
        if not last % gcd:
            return [gcd * x if x != k else last for x in range(1, k + 1)]
    return []
