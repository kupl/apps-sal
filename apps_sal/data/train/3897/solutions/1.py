def solve(n, k):
    return 2 * (n - k - 1, k + 0.5)[k < n // 2]
