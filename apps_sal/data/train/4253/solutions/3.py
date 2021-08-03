def solve(n, k):
    if n <= 0:
        return []
    if k == 1:
        return [n]
    s = k * (k + 1) // 2
    for d in range(n // s, 0, -1):
        if n % d != 0:
            continue
        return [d * i for i in range(1, k)] + [n - k * (k - 1) // 2 * d]
    return []
