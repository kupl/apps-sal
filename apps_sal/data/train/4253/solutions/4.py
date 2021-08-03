def solve(n, k):
    b, r = 2 * n // (k * (k + 1)), 1
    if not b:
        return []
    for x in range(1, int(n**0.5) + 1):
        if n % x:
            continue
        if r < x <= b:
            r = x
        if r < n // x <= b:
            r = n // x
    return [r * i for i in range(1, k)] + [n - (r * k * (k - 1) // 2)]
