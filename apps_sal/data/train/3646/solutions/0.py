def fixed_points_perms(n, k):
    if k > n:
        return 0
    if k == n:
        return 1
    if k == 0:
        def subf(n): return 1 if n == 0 else n * subf(n - 1) + (-1)**n
        return subf(n)
    return fixed_points_perms(n - 1, k - 1) * n // k
